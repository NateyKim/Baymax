"""Camera models run in a child process: frames in, plain landmarks out, errors survive."""
from functools import partial
import io
import os
from pathlib import Path
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from features.vision_process import Point, Remote
from features.pose.backend import ChildPose

FAKE = textwrap.dedent('''
    from types import SimpleNamespace

    class Model:
        def detect(self, frame):
            print("library chatter on stdout")  # Must not corrupt the reply pipe.
            if frame == "boom":
                raise ValueError("bad frame")
            if frame is None:
                return None
            return [SimpleNamespace(x=frame, y=0.5, z=0.0, visibility=None, presence=0.9)]

    class NativeChatter:
        """Writes to file descriptor 1 as a C library does (librknnrt logs while it loads)."""
        def __init__(self):
            import os
            os.write(1, b"I RKNN: init done\\n")

        def detect(self, frame):
            import os
            os.write(1, b"W RKNN: query\\n")
            return None

    class Broken:
        def __init__(self):
            raise ImportError("no mediapipe")

    class Switching:
        """Starts on the NPU; a frame can make it fail over to the CPU, as FallbackBackend does."""
        device = "NPU"

        def detect(self, frame):
            if frame == "switch":
                self.device = "CPU"
            return None

    class FakeCpu:
        """create_pose_backend's cpu_factory: echoes each timestamp in x."""
        name, device = "CPU (fake)", "CPU"

        def detect(self, frame, timestamp_ms):
            return [SimpleNamespace(x=float(timestamp_ms), y=0.0, z=0.0, visibility=1.0, presence=1.0)] * 33

        def close(self):
            pass
''')


class VisionProcessTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        Path(directory.name, "fake_vision_model.py").write_text(FAKE)
        old = os.environ.get("PYTHONPATH")
        os.environ["PYTHONPATH"] = directory.name + (os.pathsep + old if old else "")
        self.addCleanup(lambda: os.environ.__setitem__("PYTHONPATH", old) if old else os.environ.pop("PYTHONPATH"))
        sys.path.insert(0, directory.name)
        self.addCleanup(sys.path.remove, directory.name)
        import fake_vision_model
        self.fake = fake_vision_model

    def test_landmarks_come_back_as_plain_points_and_errors_do_not_stop_the_process(self):
        with Remote(self.fake.Model) as model:
            self.assertEqual(model.detect(0.25), [Point(0.25, 0.5, 0.0, 0.0, 0.9)])
            self.assertIsNone(model.detect(None))
            with self.assertRaisesRegex(RuntimeError, "bad frame"):
                model.detect("boom")
            self.assertEqual(model.detect(0.75)[0].x, 0.75)
        self.assertIsNotNone(model.child.poll())  # Closed: the child has exited.

    def test_native_writes_to_stdout_do_not_corrupt_the_reply_pipe(self):
        with Remote(self.fake.NativeChatter) as model:
            self.assertIsNone(model.detect("frame"))
            self.assertIsNone(model.detect("frame"))

    def test_an_unreadable_reply_is_a_runtime_error_like_a_stopped_process(self):
        # The camera thread restarts the child on RuntimeError; anything else ended the thread.
        import threading
        for garbage in (b"I RKNN: init done\n", b"c no_such_module\nthing\n", b"\x80\x05K\x01."):
            model = Remote.__new__(Remote)
            model.lock = threading.Lock()
            model.child = type("Child", (), {"stdin": io.BytesIO(), "stdout": io.BytesIO(garbage)})()
            with self.subTest(garbage=garbage), self.assertRaises(RuntimeError):
                model.detect("frame")

    def test_a_model_that_cannot_load_raises_and_leaves_no_process(self):
        with self.assertRaisesRegex(RuntimeError, "no mediapipe"):
            Remote(self.fake.Broken)

    def test_the_models_device_comes_back_with_each_frame(self):
        with Remote(self.fake.Switching) as model:
            self.assertEqual(model.device, "NPU")
            self.assertIsNone(model.detect("frame"))
            self.assertEqual(model.device, "NPU")
            model.detect("switch")                 # read after detect: the switch happens inside it
            self.assertEqual(model.device, "CPU")
        with Remote(self.fake.Model) as model:     # a model without .device (fall toolkit's CpuPose)
            self.assertIsNone(model.device)
            model.detect(0.5)
            self.assertIsNone(model.device)

    def test_the_core_pose_backend_runs_in_the_child_with_increasing_timestamps(self):
        # =cpu makes it deterministic even on an RK3588 with converted models.
        with patch.dict(os.environ, {"BAYMAX_POSE_BACKEND": "cpu"}), \
                Remote(partial(ChildPose, None, cpu_factory=self.fake.FakeCpu)) as pose:
            self.assertEqual(pose.device, "CPU")
            stamps = []
            for _ in range(5):
                landmarks = pose.detect(None)
                self.assertEqual(len(landmarks), 33)
                self.assertIsInstance(landmarks[0], Point)
                stamps.append(landmarks[0].x)
            self.assertEqual(pose.device, "CPU")
        self.assertEqual(stamps, sorted(set(stamps)))   # strictly increasing
        self.assertIsNotNone(pose.child.poll())


if __name__ == "__main__":
    unittest.main()

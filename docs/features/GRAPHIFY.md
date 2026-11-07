# Graphify: working protocol before code details

The graph gives highest-priority entry points to [the working protocol](../WORKING_PROTOCOL.md),
AGENTS, contribution rules, testing stages and update-channel authority. The graph
report and interactive viewer link there first. Agent instructions require the
query wrapper below; the wrapper prints the protocol before Graphify's answer.

```bash
python -m pip install -r devops/graphify/requirements.txt
python devops/graphify/query.py "Which branch should my feature PR target?"
```

To rebuild the public source map after changing protocol sources:

```bash
python devops/graphify/build.py
python devops/graphify/check.py
python -m unittest discover -s devops/graphify -p 'test_*.py'
```

The builder uses Graphify's structural extraction, native graph, clustering,
report and viewer. Reviewed protocol relationships are source-linked in
`docs/features/semantic_graph.json`; governance edges express documented review
rules, not runtime calls. No model/provider request or hardware capture occurs.
The public graph excludes dependencies, credentials, private runtime data,
recordings, SD images and review logs. External/unresolved references are reported
separately and are not proof of missing packages.

CI runs a standard-library protocol-map checker: missing graph entries, stale
normalized source hashes or a missing protocol priority entry fail the check.
This validates the protocol map, not every runtime relationship or whether a
human/LLM actually read the rules. Repository instructions apply to contributors;
no software can force unrelated external LLMs to follow those instructions.

`graphify-out/START_HERE.md` is the portable first-read copy;
`graphify-out/graph.json` has explicit `protocol_entrypoints` priority metadata.
The interactive HTML is a local file, not a live hosted site. Graph presence is
not software, chamber, hardware or deployment approval.

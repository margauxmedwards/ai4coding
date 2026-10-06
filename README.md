# How to get the most out of your tokens

Two complementary presentations by Margaux Edwards, QUT Centre for Robotics. Originally presented June 2026; updated 6 October 2026.

| Presentation | Audience | Progression |
|---|---|---|
| [Beginner](https://margauxmedwards.github.io/ai4coding/presentation/) | Can read basic code; new to coding agents | Setup → vocabulary → tools/models → task brief → worked bug fix → review/undo → first skill |
| [Advanced](https://margauxmedwards.github.io/ai4coding/) | Can review diffs and run tests | Repeated research process → tool contract → known-answer checks → skill → provenance → tools/models → workflow evaluation |

## View and maintain

Open `index.html` or `presentation/index.html` in a browser. Keep the `assets/` directory alongside them. There is no build step or external runtime dependency. The pages also work without JavaScript; JavaScript only closes the contents menu after navigation.

Serve locally if preferred: `python3 -m http.server 8000`.

Edit the HTML directly and use `assets/presentation.css` for shared styling. Both presentations contain dated, linked official sources. Recheck those sources before refreshing model names. Distinguish a model comparison from a comparison of entire tools; no original benchmark results are claimed here.

## Beginner exercise

Download or copy `examples/first-task/` to a disposable folder. With Python 3, run:

```sh
cd examples/first-task
python3 -m unittest -v
```

One test intentionally errors on empty input. The learner asks an agent for the smallest fix, then reruns all three tests and reviews the diff. Keep expected test results unchanged. The presentation shows the expected fix.

## Advanced research workflow

The advanced talk follows a repeatable experiment comparison: capture the procedure, develop a small validation/aggregation tool, test known-answer and invalid fixtures, and wrap the verified tool in a `compare-experiments` skill. It also covers dataset validation, literature matrices, figure generation and research provenance.

The CLI, repository layout and skill shown in this talk are illustrative designs to implement in a research repository. This presentation does not ship a comparison tool or install a skill. The small numerical table is a teaching fixture, not a research finding.

`examples/rosbag-sample.pbs` remains a legacy teaching example from the earlier HPC version; it is not part of the current talk and is not a verified cluster job.

## What changed

- Gave the talks distinct learning paths and links between them.
- Added a runnable beginner exercise, verification and undo guidance.
- Compared Copilot, Claude Code, Codex and Gemini CLI separately from their models.
- Added a dated model shortlist and a controlled evaluation method.
- Corrected skill structure, portability, lifecycle hook and memory claims.
- Replaced unsupported fixed credit figures with actual-usage measurement.
- Refocused the advanced talk on developing research tools and skills, with validation fixtures, provenance and a worked improvement loop.
- Replaced opaque HTML bundles with accessible static HTML and shared responsive CSS while retaining the dark terminal-inspired style.

The original design was developed from Canva slides with ChatGPT and Claude review and Claude Design. The updated pages retain the original presentation theme.

# How to get the most out of your tokens

Two complementary follow-along guides by Margaux Edwards, QUT Centre for Robotics. Both use Ask → Plan → Act to explain how useful context, clear goals and reusable procedures improve the value of a coding session. The guidance is model-agnostic.

| Presentation | Audience | Progression |
|---|---|---|
| [Beginner](https://margauxmedwards.github.io/ai4coding/presentation/) | Can read basic code; new to coding agents | Token value → Ask / Plan / Act → relevant context → worked bug fix → review → reusable context |
| [Advanced](https://margauxmedwards.github.io/ai4coding/) | Can review diffs and run tests | Ask / Plan / Act for research → repeated processes → tools → checks → skills → context → less rework |

## View and maintain

Open `index.html` or `presentation/index.html` in a browser. Keep the `assets/` directory alongside them. There is no build step or external runtime dependency. The pages also work without JavaScript; JavaScript only closes the contents menu after navigation.

Serve locally if preferred: `python3 -m http.server 8000`.

Edit the HTML directly and use `assets/presentation.css` for shared styling. Both guides focus on lasting workflow principles. Tool-specific skill examples link to implementation documentation; use the locations and loading rules supported by your own tool.

## Beginner exercise

Download or copy `examples/first-task/` to a disposable folder. With Python 3, run:

```sh
cd examples/first-task
python3 -m unittest -v
```

One test intentionally errors on empty input. The learner asks an agent for the smallest fix, then reruns all three tests and reviews the diff. Keep expected test results unchanged. The presentation shows the expected fix.

## Advanced research exercise

The advanced talk follows a repeatable experiment comparison: capture the procedure, develop a small validation/aggregation tool, test known-answer and invalid fixtures, and wrap the verified tool in a `compare-experiments` skill. It also covers dataset validation, literature matrices, figure generation and research provenance.

The CLI, repository layout and skill shown in this talk are illustrative designs to implement in a research repository. Downloadable fixtures live in `examples/research/runs.csv` and `examples/research/evaluation.json`. Readers build the comparison tool with their coding assistant, check its arithmetic and failure cases, then wrap the verified process in a skill. The site does not ship that tool or install a skill. All example measurements are invented teaching data.

`examples/rosbag-sample.pbs` remains a legacy teaching example from the earlier HPC version; it is not part of the current talk and is not a verified cluster job.

## What changed

- Gave the talks distinct learning paths and links between them.
- Added a runnable beginner exercise, verification and undo guidance.
- Restored the shared title and Ask → Plan → Act as the organising idea of both talks.
- Removed dated model lists and vendor comparisons; focused on context, goals, verification and avoided rework.
- Corrected skill structure, portability, lifecycle hook and memory claims.
- Replaced unsupported fixed credit figures with actual-usage measurement.
- Refocused the advanced talk on developing research tools and skills, with validation fixtures, provenance and a worked improvement loop.
- Replaced opaque HTML bundles with accessible static HTML and shared responsive CSS while retaining the dark terminal-inspired style.

The original design was developed from Canva slides with ChatGPT and Claude review and Claude Design. The updated pages retain the original presentation theme.

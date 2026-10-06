# How to get the most out of your tokens

Two complementary presentations by Margaux Edwards, QUT Centre for Robotics. Originally presented June 2026; updated 6 October 2026.

| Presentation | Audience | Progression |
|---|---|---|
| [Beginner](https://margauxmedwards.github.io/ai4coding/presentation/) | Can read basic code; new to coding agents | Setup → vocabulary → tools/models → task brief → worked bug fix → review/undo → first skill |
| [Advanced](https://margauxmedwards.github.io/ai4coding/) | Can review diffs and run tests | HPC context → success criteria → checkpoints → PBS template → customisation → tools/models → evaluation → cost/handoffs → verified lessons |

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

## Advanced example

`examples/rosbag-sample.pbs` is the same teaching template displayed in the advanced presentation. It is **not a verified Aqua job**. Confirm the queue, resources, scratch variable, environment and project tasks before submission. Its two `pixi` tasks are explicit project adapters, not commands provided by this repository. No cluster job is submitted by this site.

The marker `COMPLETE` is written only after conversion validation and copy-back succeed. The validation task must implement the project's actual data checks. Job submission alone does not establish success.

## What changed

- Gave the talks distinct learning paths and links between them.
- Added a runnable beginner exercise, verification and undo guidance.
- Compared Copilot, Claude Code, Codex and Gemini CLI separately from their models.
- Added a dated model shortlist and a controlled evaluation method.
- Corrected skill structure, portability, lifecycle hook and memory claims.
- Replaced unsupported fixed credit figures with actual-usage measurement.
- Made the PBS example's site dependencies and completion criteria explicit.
- Replaced opaque HTML bundles with accessible static HTML and shared responsive CSS while retaining the dark terminal-inspired style.

The original design was developed from Canva slides with ChatGPT and Claude review and Claude Design. The updated pages retain the original presentation theme.

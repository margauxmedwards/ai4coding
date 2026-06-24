# How to get the most out of your tokens

**Context-driven AI for any model**
> *Tips and tricks from setting up a robotics pipeline*
> Margaux Edwards · QUT Centre of Robotics · June 2026

---

## Talk

The presentation is a self-contained HTML file. Open `index.html` in any browser — no build step, no server required.

**Live:** [margauxmedwards.github.io/ai4coding](https://margauxmedwards.github.io/ai4coding)

---

## Contents

| Section | Topic |
|---|---|
| 01 | Without context, the model guesses |
| 02 | Prompting vs context |
| 03 | Be specific about success |
| 04 | Ask · Plan · Act |
| 05 | Constrain the output format + choose the right model |
| 06 | Before / after — PBS job with and without context |
| 07 | The repository as a prompt scaffold |
| 08 | Agent customisations — agents, skills, instructions, hooks, MCP, plugins |
| 09 | Practical prompt template |
| 10 | Key takeaways + limitations |

---

## Key ideas

**Better context beats longer prompts.**
Structure what the model needs to know in files — not in the chat window.

**Repositories are durable context windows.**
A repo with `copilot-instructions.md`, skill files, and `AGENTS.md` carries context that chat history forgets.

**Make success observable.**
Define what done looks like before the model starts. Ask for visible artifacts — plans, commands run, files changed, rollback paths.

**Use Ask → Plan → Act.**
Match the mode to the task. Don't act until you've asked and planned.

**The cheapest model that reliably does the job is the right model.**
Better context reduces variance — and variance is what forces you to reach for the expensive model.

**Restarting a fresh chat is often cheaper than continuing a long one.**
Once context lives in the repo, the model picks up exactly where it left off.

---

## Limitations

No model tells you upfront how many tokens a task will consume. Usage only becomes visible after the fact.

Real numbers from the GitHub Copilot AI credit system:

| Task | Credits |
|---|---|
| Single file edit | 100+ |
| Write a PR description | ~30 |

Better context = fewer retries = fewer credits spent.

---

## The context stack (from my `tools/`)

```
.github/
├── copilot-instructions.md   # always active — repo-wide system prompt
├── instructions/             # file-aware — applied by glob pattern
│   ├── ros2-python.md
│   ├── hpc.md
│   └── pixi.md
├── skills/                   # on demand — loaded for specific tasks
│   ├── hpc-core/SKILL.md
│   ├── pbs-jobs/SKILL.md
│   └── wandb-hpc/SKILL.md
└── agents/
    └── vpr-pipeline.agent.md

AGENTS.md                     # agent-level guardrails
.env.example                  # config template — never commit secrets
```

These customisations work across models: Claude, Copilot (Azure), self-hosted — including VS Code extensions and GitHub integrations.

---

## References

- [QUT Aqua HPC documentation](https://docs.eres.qut.edu.au/about-aqua)
- [GitHub Copilot agent customisations](https://docs.github.com/en/copilot/customizing-copilot)

This presentation was built initially as a set of Canva Slides, which were then given to ChatGPT and Claude for review and comparision. Claude Design was then used to build the html site.

# Aha

[简体中文](README.md) | **English**

**Let understanding come naturally.**

Aha is a skill that explains the point where you are stuck. It works in Codex and in Claude. When a concept, a step in a derivation, or a piece of code doesn't make sense while you are reading, coding, or studying, bring it into the conversation. Aha starts from what you already understand and connects the new idea to it step by step.

> v0.2.0 · Public preview. Try it and share your feedback.

## The problem it solves

Many explanations are correct, yet you still can't follow them. Usually the explanation skips something you don't have yet:

- **The starting point**: it doesn't begin from what you already understand, or it builds on something you have wrong.
- **The steps**: a step the explainer finds obvious goes unexplained, or an example jumps from input to output.
- **The meaning**: a technical term or symbol stands in for the explanation it was supposed to name.

Aha does one thing: at the one point where you are stuck, it fills in what was skipped, then hands the pace back to you. It does not take over your study session, plan lessons, or set exercise sets.

## When it applies

- You ask what a term, passage, symbol, or piece of code means.
- You ask why or how something works, or why a step in a derivation follows.
- You ask how two ideas relate or differ.
- You say an explanation is unclear or too abstract, whether it came from Aha, a textbook, a lecturer, or another AI.
- You state an understanding that is wrong, such as "Do race conditions happen because each thread has its own copy?"
- You get stuck in the middle of a task because of something you don't understand, such as an error message. Aha explains the cause briefly, then finishes the task.

You don't need to name Aha or pinpoint exactly what confuses you.

Aha does not apply to pure execution (writing code, reformatting), quick lookups (the argument order of a function), opinions or decisions ("which database should I use?"), or requests that run a whole study session, such as quizzes, flashcards, or study plans.

## How it explains

- **Picks up from what you said**: it starts from what you already understand and doesn't re-explain it.
- **Gives terms a meaning at first use**: a term you haven't used gets a short gloss the first time it appears.
- **Walks one example through the intermediate states**: it shows what happens at each step, not just the input and the result.
- **Names the common misconception**: if many people hold a particular wrong model, it addresses it directly.
- **Lands the conclusion**: it ends by stating the core relationship in a sentence or two.
- **May leave a quick check**: after explaining a central mechanism, it may put one question on the last line that changes one condition, so you use what you just learned. You can skip it and carry on.

You can state what you want at any time:

> "Just tell me the answer."
>
> "Don't give me the conclusion yet. Give me a hint."
>
> "That's still too abstract."
>
> "OK, let's stop here."

## Your first conversation

After installing, start with a real question. For example:

```text
I know threads share memory, but I don't understand why that leads to race conditions.
```

You can also bring material you are reading:

```text
I can follow the first two steps of this derivation, but I don't see why the third step follows.

[Paste the relevant material]
```

To request Aha explicitly, use `$aha` in Codex or `/aha` in Claude Code.

## Installation

Aha contains only instruction files, so it requires no API key or service. Conversations use the model you select in Codex or Claude.

### Codex

Option 1: send the following message to Codex.

```text
Please use $skill-installer to install Aha v0.2.0:
https://github.com/CatDisgust/aha-skill/tree/v0.2.0/skills/aha
```

Option 2: download [aha-v0.2.0.zip](https://github.com/CatDisgust/aha-skill/releases/download/v0.2.0/aha-v0.2.0.zip), extract the `aha` folder, and place the whole folder in your user-level skills directory, `~/.agents/skills/`. Confirm that the instructions are at `~/.agents/skills/aha/SKILL.md`.

If Codex does not recognize the skill after installation, restart Codex and try again. For directory details, see the [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code

Download and extract [aha-v0.2.0.zip](https://github.com/CatDisgust/aha-skill/releases/download/v0.2.0/aha-v0.2.0.zip), then place the `aha` folder in `~/.claude/skills/`. Confirm that the instructions are at `~/.claude/skills/aha/SKILL.md`. For directory details, see the [Claude Code documentation](https://code.claude.com/docs/en/skills).

### claude.ai

Download [aha-v0.2.0.zip](https://github.com/CatDisgust/aha-skill/releases/download/v0.2.0/aha-v0.2.0.zip) and upload it, without extracting, to Skills in your claude.ai settings. Code execution must be enabled. See the [Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) for the steps.

`~` means your user home directory. Install one copy per platform; don't install it in more than one skills directory.

### Upgrading from v0.1

Move the old `aha` folder outside the skills directory as a backup, then put the new `aha` folder in the same location. To roll back, restore the backup.

v0.2 changes what Aha is for. Before upgrading, note these differences:

- **It handles one explanation**: v0.1 ran a whole tutoring session, with an opening, three phases, a closing recap, and pausing when you were tired. v0.2 only explains the current sticking point and leaves the pace of study to your platform's learning mode or to you.
- **It says when not to apply**: it explicitly excludes pure execution, quick lookups, opinions, and session management.
- **The check question follows fixed rules**: at most one per explanation, on the last line, with a clear answer. It is skipped when you only want the answer, are in a hurry, or didn't answer the previous one.
- **It is half the size**: the instruction file went from about 20KB to about 10KB.

## Design basis

Aha draws on cognitive load theory and self-determination theory. An explanation should reduce the effort you spend decoding the explanation itself, while leaving the work of using the idea once to you, so that reading fluently isn't mistaken for understanding. Your explicit requests, such as asking for the answer, a hint, or a stop, always take priority over the default way of explaining. The theory is recorded here as design background; SKILL.md keeps only the concrete behaviors it leads to.

## Status and feedback

- The skill has passed format checks, and the source files have been checked against the distribution package.
- v0.2.0 was checked on Claude with 24 test cases covering requests that should trigger it, requests that should not, gray areas, single rules, and multi-turn conversations. The tests used Claude subagents, one run per case; 23 behaved as expected.
- Known issue: simple definition questions such as "What does HTTP 404 mean?" may trigger Aha and get a longer explanation than needed.
- v0.2.0 has not yet been systematically tested in Codex. Independent understanding, transfer, and long-term learning outcomes have not been systematically evaluated.

Actual behavior depends on the model, the conversation context, and the question.

Share your experience through [GitHub Issues](https://github.com/CatDisgust/aha-skill/issues/new?template=feedback.md):

- What were you trying to understand, and where were you stuck?
- Which explanation helped, and which made things more confusing?
- What can you now explain or continue with, or where are you still stuck?
- Which platform (Codex or Claude), model, and Aha version did you use?

A few sentences or a short conversation excerpt with personal information removed is enough. You don't need to share your full chat history.

## License

[MIT License](LICENSE) © 2026 CatDisgust.

Use, modification, redistribution, and commercial use are permitted. Retain the license and copyright notice.

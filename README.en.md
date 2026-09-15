# Aha

[简体中文](README.md) | **English**

**Let understanding come naturally.**

Aha is a Codex skill that helps you build understanding. When you get stuck while reading, writing code, or learning a concept, bring that sticking point into the conversation. Start from what you already understand and work through the key connections, underlying mechanisms, and the “why.”

> v0.1.0 · Public preview

## When to use it

When you find yourself in situations like these:

- You remember a definition but cannot explain why something works that way.
- You reach a step in a derivation but cannot see why that step follows.
- Your code runs, but you do not yet understand the design behind it.
- You know “this part is unclear” but cannot pinpoint what is missing.

Bring your question, relevant material, or current thinking to Aha. You do not need to diagnose your exact sticking point before starting.

The first version focuses on computer science, artificial intelligence, software engineering, and systems concepts.

## Your first conversation

After installing, start with a real question. For example:

```text
Use $aha to help me understand processes and threads.
I know the definitions, but I don't understand why shared memory can lead to race conditions.
```

You can also bring material you are reading:

```text
Use $aha to help me understand the passage below.
I can follow the first two steps, but I don't see why the third step follows.

[Paste the relevant material]
```

See [Installation](#installation) below for setup instructions.

## How it helps

Aha uses your question, existing understanding, and feedback during the conversation to choose a suitable form of support:

- **Build a framework:** See what problem a concept addresses and where it fits in the broader system.
- **Explain the mechanism:** Work through key steps and causal relationships, filling in relevant foundations.
- **Use examples and analogies:** Start with a familiar situation, then connect it back to the actual concept.
- **Use questions to support reasoning:** When you want to reason further, explore connections and examine assumptions.

If an explanation or question is not helping, Aha adjusts the scope, pace, or type of support based on your feedback. You can also state your preferences directly:

> “Explain the whole process first. I want to see the big picture.”
>
> “I couldn't follow that analogy. Try a more familiar example.”
>
> “Don't give me the conclusion yet. Give me a hint.”
>
> “I'm getting tired. Let's stop here for now.”

Aha aims to provide enough support for you to gradually explain the connections yourself, understand why they hold, and continue your original learning or work.

## Installation

You need a working Codex setup and permission to install local skills. Aha itself contains only instructions and display metadata, so it requires no additional API key or service. Conversations use the model you select in Codex.

### Option 1: Ask Codex to install it

Send the following message to Codex:

```text
Please use $skill-installer to install Aha v0.1.0:
https://github.com/CatDisgust/aha-skill/tree/v0.1.0/skills/aha
```

### Option 2: Install the ZIP manually

1. Download [aha-v0.1.0.zip](https://github.com/CatDisgust/aha-skill/releases/download/v0.1.0/aha-v0.1.0.zip) and extract the `aha` folder.
2. Place the entire `aha` folder in your user-level skills directory, `~/.agents/skills/`. Create that directory if it does not exist.
3. Confirm that the instructions are at `~/.agents/skills/aha/SKILL.md`.

`~` means your user home directory. Choose either installation method; you do not need both.

After installation, use `$aha` in your next message to start a conversation. If Codex does not recognize it, restart Codex and try again.

For installation and directory details, see the [official Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).

## Status and feedback

- The skill has passed format checks, and the source files have been checked against the distribution package.
- Explicit invocation, direct-explanation requests, and pause requests were checked using Codex CLI 0.153.4 / gpt-6-astra.
- Learning outcomes have not been systematically evaluated.
- This version provides instructions for Codex; compatibility with other tools has not been verified.

“Let understanding come naturally” describes the experience we aim to create. Actual behavior depends on the model, conversation context, and question.

Share your experience through [GitHub Issues](https://github.com/CatDisgust/aha-skill/issues/new?template=feedback.md):

- What were you trying to understand, and where were you stuck?
- Which explanation or question helped, and which made things more confusing?
- What can you now explain or continue with, or where are you still stuck?
- Which Codex, model, and Aha versions did you use?

A few sentences or a short conversation excerpt with personal information removed is enough. You do not need to share your full chat history.

## License

[MIT License](LICENSE) © 2026 CatDisgust.

Use, modification, redistribution, and commercial use are permitted. Retain the license and copyright notice.

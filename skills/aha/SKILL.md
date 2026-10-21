---
name: aha
description: Explain a concept, step, passage, or piece of code someone is stuck on, so they can actually follow it and use it. Use whenever the user asks what something means, why or how something works, why a step follows, or how two ideas relate, or says an explanation is unclear, too abstract, or still doesn't click — even if they never mention Aha or can't say exactly what confuses them. In a mixed task, fix the understanding gap briefly, then keep doing the task. Not for pure execution, quick lookups, opinions, or running tutoring sessions, quizzes, or study plans; see the body for details.
metadata:
  version: "0.2.0"
  status: initial-trial
---

# Aha

让理解自然发生。

## Why this exists

Explanations often skip what the student doesn't have yet. What is obvious to the explainer is exactly where the student gets stuck. Aha closes that gap: it starts from what the student already understands and connects the new idea to it step by step, so they can follow it and explain it themselves.

Three things get skipped, and the rest of this skill is about not skipping them:

- **The starting point.** The explanation begins from where the explainer stands rather than from what the student already understands, or it builds on something the student has wrong.
- **The steps.** A transition the expert finds obvious goes unexplained, or an example jumps from input to output without the states in between.
- **The meaning.** A technical term or symbol stands in for the explanation it was supposed to name.

Aha explains one stuck point and then steps back. Pacing, review, and practice belong to the host's learning mode or to the user.

## When to use

Use Aha when the student is trying to understand something specific, for example when they:

- ask what a term, passage, symbol, or piece of code means;
- ask why or how something works, or why it behaves the way it does;
- ask why a step in a proof, derivation, or argument follows;
- ask how two ideas relate or differ;
- say an explanation is unclear, too abstract, or still doesn't click;
- hit an understanding gap in the middle of a task (for example, an error they don't understand). Explain the gap briefly, then continue the task.

The student doesn't need to name Aha or pinpoint what confuses them.

## When not to

Default to not using Aha when the student isn't trying to understand something. Each exclusion below exists because an explanation there would add friction instead of removing it.

- **Pure execution** (write, fix, convert, run) with no sign of an understanding gap. An unrequested explanation slows down the work they asked for.
- **Quick lookups** (a definition, a value, a syntax reminder). They want the fact. Give it plainly. If they then ask why, or say it doesn't make sense, use Aha.
- **Requests for an opinion or a decision** ("which should I use?"). That is weighing options, not building understanding. If they ask how the options work so they can decide, use Aha for that part.
- **Running the session**: tutoring sessions, quizzes, flashcards, study plans, or a requested pace. These belong to the host's learning mode or a dedicated tool, and Aha's rules would conflict with them.
- **Creative writing and casual chat.** There is nothing to explain.

Gray areas:

- **"Just tell me the answer."** Still Aha: give the complete answer with the reasoning that makes it make sense, and skip the check question.
- **The student checks their own understanding** ("so it's X, right?"). If they are right, confirm in a sentence and add only what's missing. Don't re-explain what they already have.
- **"What is X?" from someone already using X** (in their code or argument). They are probably stuck on how it applies there, not on the dictionary definition. Explain it in their context.

## How to explain

### Find the starting point

Judge only from evidence in the conversation: the student's own words, what they say they know and don't, the material they are working with, and earlier turns.

- **Specific gap, framework in place** ("I know threads share memory, but why does that cause races?"): explain that gap directly, starting from what they named. Don't restart the topic. Extra material buries the part they need.
- **Whole concept, no visible framework** ("what is a race condition?"): first give a compact model in a few sentences (the problem it addresses, why it arises, the mechanism, the result), then the part they asked about.
- **Evidence of a broken prerequisite** (they misstate a basic fact or misuse a basic term): repair that piece briefly, then return to the question.
- **No evidence either way about a prerequisite:** don't pre-teach it. Gloss it at first use instead (below). Being unfamiliar with the target concept is not a broken prerequisite.

Ask before explaining only when the thing to explain is missing (no code, formula, or passage to look at), or when two readings would lead to completely different explanations. Otherwise state your assumption in one clause and explain. The student can correct you in one line, which costs far less than waiting for an answer.

### Build the explanation

1. **Bridge every unfamiliar transition.** For each step the student can't yet make, say what is involved, what changes, why, and what that establishes. Merge the steps they can already make.
2. **Give every unfamiliar term a meaning at first use.** Treat terms the student used correctly as known. For any other term, add a short gloss the first time it appears. A term names an idea; it never replaces explaining it.
3. **Carry one simple example through the mechanism.** Show the intermediate states, not just input and output. Say which part generalizes and which belongs only to the example. For an analogy, start from something familiar, keep the key relationship, map it back to the real concept, and say where it breaks.
4. **Name the likely misconception.** If there is a common wrong model, address it directly ("It's tempting to think X; actually Y, because …"). Students who hold it without realizing are the ones who need this most.
5. **Land the conclusion.** Finish by stating the core relationship plainly in a sentence or two.

### Follow the student's lead

- They ask for a hint, or say they want to work it out: give the smallest hint that lets them take the next step, without revealing it.
- They say it still doesn't click: keep what they already understood and change one real thing. Supply a missing prerequisite, show intermediate states you skipped, switch to a more familiar example, or change the representation. Rephrasing the same abstraction with synonyms only costs them more effort.
- They want to stop or move on: stop.

### Example

Student: "I know threads share memory, but I don't get why that causes race conditions."

A weak answer: "Because `count++` isn't atomic, which leads to a data race." It is correct, but two new terms stand in for the explanation.

An Aha answer starts from shared memory and walks one case: `count` is 5; thread A reads 5; before A writes back, thread B also reads 5; both compute 6 and both write 6. Two increments happened, one was lost. It then names the mechanism: `count++` is really three steps (read, add, write), and the gap between read and write is where the other thread slips in. It glosses "atomic" as "can't be interrupted partway", addresses the common belief that any simultaneous access is the problem, and states the conclusion.

## Check question

Reading an explanation feels like understanding; using it is the test. After explaining a central mechanism, you may end with one short question that makes the student use it.

Build it from your own explanation: list the conditions the mechanism depends on, change one, and ask what happens. Prefer the condition whose wrong answer would reveal a common misconception. In the example above: "If one thread only reads `count` and the other increments it, can an update still be lost?"

Rules:

- At most one check question per explanation.
- Ask it only if it can't be answered by recalling your wording, needs no knowledge you haven't given, has one clear answer you are certain of, and a wrong answer would show which part is missing. If any of these fails, skip it.
- Skip it when the student asked for just the answer, is in a hurry, or the previous reply's check question went unanswered.
- Put it on the last line, starting with a short lead-in in the student's language (for example "Quick check:" / "顺带想一下："). Write nothing after it.
- If they answer correctly, say specifically what they worked out. If they answer wrongly, say clearly which part is right and which is wrong, then fix that gap once. Don't start another round of questions unless they ask for one.

## Output format

- Reply in the language the student is using. Example phrasings in this skill are illustrations; adapt them naturally instead of translating them literally.
- Write connected prose. Use a list, table, or small diagram only when it makes the relationships easier to see. Use no headings in a short answer.
- Size the answer to the gap: a local question gets a short answer.
- Ask at most one question per response: either the clarifying question or the check question, never both.
- End with the conclusion, or with the check question if you include one. Don't append generic offers of more help.
- Praise only something specific the student actually worked out.

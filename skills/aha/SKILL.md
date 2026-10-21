---
name: aha
description: Explain a concept, step, passage, or piece of code someone is stuck on, so they can actually follow it and use it. Use whenever the user asks what something means, why or how something works, why a step follows, or how two ideas relate, or says an explanation is unclear, too abstract, or still doesn't click — even if they never mention Aha or can't say exactly what confuses them. In a mixed task, fix the understanding gap briefly, then keep doing the task. Not for pure execution requests, and not for running tutoring sessions, quizzes, or study plans.
metadata:
  version: "0.2.0"
  status: initial-trial
---

# Aha

让理解自然发生。

Aha does one job: when someone is stuck on a specific idea, it builds an explanation they can follow, starting from what they already understand. A good Aha answer removes friction, so the student spends their effort on the idea itself rather than on decoding the explanation.

## Scope

Aha shapes a single explanation. It does not run the session: no opening greeting, lesson phases, recaps, exercise sequences, or study plans. If the host or the user has set a learning mode or a pace, follow it; Aha only governs how the stuck point gets explained.

Reply in the language the student is using. Example phrasings below are illustrations; adapt them naturally instead of translating them literally.

## Rules

These hold in every Aha response. Each one replaces a default habit that creates friction.

1. **Answer the gap that was asked.** Explain the specific step, term, or relation the student is stuck on. Don't restart the topic or open side branches; extra material buries the part they need.
2. **Don't stall on questions.** Ask before explaining only when the thing to explain is missing (no code, formula, or passage to look at) or when two readings would lead to completely different explanations. Otherwise state your assumption in one clause and explain; the student can correct you in one line.
3. **Give every unfamiliar term a meaning at first use.** Treat terms the student used correctly as known. For any other term the explanation needs, add a short gloss the first time it appears. A term names an idea; it never replaces explaining it.
4. **Follow the student's explicit choices.** If they ask for the answer, give the complete explanation. If they ask for a hint or say they want to work it out, give the smallest hint that lets them take the next step, without revealing it. If they want to stop, stop.
5. **When it still doesn't land, change substance, not wording.** Keep what they already understood and change one real thing: supply a missing prerequisite, show intermediate states you skipped, switch to a more familiar example, or change the representation. Rephrasing the same abstraction with synonyms only costs them more effort.
6. **Keep feedback honest.** Praise only something specific the student actually worked out. If they are wrong, say clearly which part is right and which part is wrong; vague softening leaves them unsure what they understand.
7. **Ask at most one question per response,** and don't end with a generic offer of more help.

## 1. Find the starting point

Use only evidence in the conversation: the student's own words, what they say they know and don't, the material they are working with, and earlier turns.

- **Specific gap, framework in place** (e.g. "I know threads share memory, but why does that cause races?"): explain that gap directly, starting from what they named.
- **Whole concept, no visible framework** (e.g. "what is a race condition?"): first give a compact model in a few sentences (the problem it addresses, why it arises, the mechanism, the result), then the part they asked about.
- **Evidence of a broken prerequisite** (they misstate a basic fact or misuse a basic term): repair that piece briefly, then return to the question.
- **No evidence either way about a prerequisite:** don't pre-teach it; gloss it at first use (rule 3). Being unfamiliar with the target concept is not a broken prerequisite.

## 2. Build the explanation

1. **Bridge every unfamiliar transition.** For each step the student can't yet make, say what is involved, what changes, why, and what that establishes. Merge the steps they can already make.
2. **Ground words and symbols.** Tie terms, symbols, and code to concrete things doing concrete actions before relying on them. Keep references unambiguous.
3. **Carry one simple example through the mechanism.** Show the intermediate states, not just input and output. Say which part generalizes and which belongs only to the example. For an analogy, start from something familiar, keep the key relationship, map it back to the real concept, and say where it breaks.
4. **Name the likely misconception.** If there is a common wrong model, address it directly ("It's tempting to think X; actually Y, because …"). Students who hold it without realizing are the ones who need this most.
5. **Land the conclusion.** Finish by stating the core relationship plainly in a sentence or two.

Prefer connected prose. Use a list, table, or small diagram only when it makes the relationships easier to see. Size the answer to the gap: a local question gets a short answer.

## 3. Optional: one check question

Reading an explanation feels like understanding; using it is the test. After explaining a central mechanism, you may end with one short question that makes the student use it.

Build it from your own explanation: list the conditions the mechanism depends on, change one, and ask what happens. Prefer the condition whose wrong answer would reveal a common misconception. Add it lightly at the end ("Quick check: …") rather than asking whether they want one.

Ask it only if all of these hold; otherwise skip it:

- it can't be answered by recalling your wording;
- it needs no knowledge you haven't given;
- it has one clear answer you are certain of;
- a wrong answer would show which part is missing.

When the student answers correctly, say specifically what they worked out. When the answer is wrong, apply rule 6 and fix the exposed gap once. Don't start another round of questions unless they ask for one.

## Example

Student: "I know threads share memory, but I don't get why that causes race conditions."

A weak answer: "Because `count++` isn't atomic, which leads to a data race." It is correct, but two new terms stand in for the explanation.

An Aha answer starts from shared memory and walks one case: `count` is 5; thread A reads 5; before A writes back, thread B also reads 5; both compute 6 and both write 6. Two increments happened, one was lost. It then names the mechanism: `count++` is really three steps (read, add, write), and the gap between read and write is where the other thread slips in. It glosses "atomic" as "can't be interrupted partway", addresses the common belief that any simultaneous access is the problem, and states the conclusion. It may end with: "Quick check: if one thread only reads `count` and the other increments it, can an update still be lost?"

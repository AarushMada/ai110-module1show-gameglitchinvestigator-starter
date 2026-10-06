# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

The game is a number-guessing challenge that gives higher/lower hints and tracks attempts and score. At first, a guess above the secret incorrectly told me to go higher, so following the hint moved me farther from the answer. Pressing Enter did not submit the input, and starting a new game did not reset all of the old game's state. I used the developer debug panel to compare the displayed secret with each result and reproduce these problems.

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess `60` with secret `50` | Show "Go LOWER!" | Showed "Go HIGHER!" | No console error |
| Type a valid guess and press Enter | Submit the guess | Nothing happened | No console error |
| Click New Game after a win or loss | Reset status, score, attempts, history, and input | Some state and input remained from the previous game | No console error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used Codex to inspect `app.py` and `logic_utils.py`, propose focused repairs, and generate a regression test. Its suggestion to move `check_guess` into `logic_utils.py` and compare integer values directly was correct because it removed the mixed string/integer branch that made the hints unreliable; I verified it with high, low, and winning `pytest` cases. I did not accept Codex's first documentation edit as written because it changed the README and added unrelated tests beyond the two Phase 2 bugs. I asked it to narrow the work, then verified the smaller diff only changed the requested code, focused test, and reflection evidence.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated a bug as fixed only when the relevant automated test passed and the same behavior worked in the Streamlit UI. Codex helped add a focused boundary regression test showing that a guess of `51` against a secret of `50` returns `Too High`, in addition to the starter tests for high, low, and exact guesses. For the reset bug, I checked that New Game creates a secret inside the selected range and clears attempts, score, status, history, and the input. I also started the Streamlit server to confirm the repaired app loaded without an exception.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

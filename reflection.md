# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

When I first ran the game, it looked normal but some of the main features did not work correctly. The higher and lower hints were reversed, pressing Enter did not submit a guess, and starting a new game did not reset everything. These bugs made the game confusing and sometimes made it impossible to keep playing.

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50 | Too high and go lower | Said to go higher | None; hint logic was in `app.py` |
| Press Enter after typing 44 | Submit the guess | Nothing happened | None; submit button was in `app.py` |
| Start a new game | Reset the entire game | Old game information was not fully reset | None; reset logic was in `app.py` |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Codex.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Codex correctly pointed out that a guess above the secret returned "Too High" but incorrectly said "Go Higher." I verified the fix by running pytest and trying guesses above and below the secret in the game.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
The AI tried implementing a whole new system to make the hints more "efficient," but I thought that this suggestion was over-engineered. I asked it to focus only on the issue that I brought up, then I verified that the smaller fix still passed the tests.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the program and checked to see if the fix was implemented correctly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest and all four tests passed. One test used a guess of 51 with a secret of 50 and showed that the hint logic returned "Too High" even when the guess was only one number away.

- Did AI help you design or understand any tests? How?
Codex helped me create the extra test and explained that it would prevent the same bug from being added again later.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the whole Python file whenever the user clicks a button or changes something. Session state saves important values so they do not disappear during each rerun. In this game, it keeps track of the secret number, attempts, score, status, and guess history until a new game is started.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is running a test after every fix instead of waiting until the end. Next time, I would give the AI a more specific prompt so it does not add extra features that I did not ask for. This project showed me that AI can help find and repair bugs, but its suggestions still need to be reviewed. AI-generated code can look correct even when the logic has mistakes, so I should always test it myself.

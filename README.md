# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the game: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The purpose of the game is to guess a secret number before running out of attempts. The game gives higher or lower hints and keeps track of the score.
- [x] I found reversed hints, an Enter key that did not submit guesses, and a New Game button that did not fully reset the game.
- [x] I moved the main game logic into `logic_utils.py`, corrected the hint comparisons, used a form for submitting guesses, and reset all session state when a new game starts.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The game chooses a secret number of 50, and the user enters a guess of 40.
2. The game returns "Too Low" and tells the user to go higher. The score changes from 0 to -5.
3. The user enters 70, and the game returns "Too High" and tells the user to go lower. The score changes to -10.
4. The user enters 50, and the game shows that the answer is correct. The final score is 60 after three attempts.
5. The user clicks **New Game**, and the attempts, score, status, history, and input are reset.

## 🧪 Test Results

```text
$ .venv/bin/python -m pytest -q
.......                                                                  [100%]
7 passed in 0.01s
```

## 🚀 Stretch Features

- [x] Challenge 1: Added tests for negative numbers, decimals, and extremely large numbers. The game now rejects these invalid guesses with a clear message without using an attempt.

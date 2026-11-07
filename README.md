# Project 02: Number Guessing Game & Word Counter

A beginner-friendly, terminal-based Python project built according to the supplied Project 02 learner guide.

## Features

### 1. Number Guessing Game
- The computer selects a random number from 1 to 100.
- You have 10 valid attempts to guess the number.
- The game displays **Too low**, **Too high**, or **Correct**.
- Invalid input and numbers outside 1–100 do not use an attempt.
- The score starts at 100 and decreases by 10 for each incorrect valid guess.
- The program tracks the best score during the current run and allows replay.

### 2. Word Counter
- Reads a text file using UTF-8 encoding and a `with` block.
- Converts text to lowercase and removes punctuation.
- Counts words with `collections.Counter`.
- Displays total words, unique words, and the 10 most common words.
- Shows a friendly message if the file cannot be found.
- Includes `sample.txt` so you can test the feature immediately.

## Project files

```text
Project-02-Number-Guessing-Game/
├── main.py
├── sample.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- VS Code or IDLE

No extra packages need to be installed. The project uses Python's standard library.

## How to run in VS Code

1. Extract the ZIP file.
2. Open the extracted `Project-02-Number-Guessing-Game` folder in VS Code.
3. Open `main.py`.
4. Open the terminal: **Terminal → New Terminal**.
5. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```bash
   py main.py
   ```

6. Choose `1` to play the game, `2` to count words, or `3` to quit.

## How to use your own text file

Place your `.txt` file in the project folder. Choose option `2` and enter its filename, for example `my_story.txt`. Press Enter without typing a filename to use the included `sample.txt`.

## Scoring rule

The score starts at **100 points**. Every incorrect valid guess reduces the score by **10 points**. Invalid entries and guesses outside the range 1–100 do not count as attempts or reduce the score. The best score is kept while the program is running.

## Example test cases

- Enter letters instead of a number: the program should show an error and continue.
- Enter `0` or `101`: the program should ask for a number from 1 to 100.
- Select option `2` and press Enter: the program should count words in `sample.txt`.
- Enter a filename that does not exist: the program should show a helpful message.
- Select option `3`: the program should exit.

## Submission checklist

- [ ] Run and test both menu options.
- [ ] Take a screenshot of one completed guessing game.
- [ ] Take a screenshot of the word-count results.
- [ ] Push the project folder to GitHub.
- [ ] Submit the GitHub link and scoring rule with the two screenshots or text outputs.

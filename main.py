import random
import string
from collections import Counter


def play_guessing_game():
    """Play a number guessing game and return the player's score."""
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    score = 100

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("You lose 10 points for each incorrect guess.")

    while attempts < max_attempts:
        remaining = max_attempts - attempts

        try:
            guess_text = input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: ").strip()
            guess = int(guess_text)

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100. This does not use an attempt.")
                continue

        except ValueError:
            print("Invalid input. Please enter a whole number, such as 25.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempt(s).")
            print(f"Your score: {score}/100")
            return score

        score = max(0, score - 10)

        if guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        print(f"Attempts remaining: {max_attempts - attempts}")
        print(f"Current score: {score}/100")

    print(f"\nGame over! The correct number was {secret_number}.")
    print("Your score: 0/100")
    return 0


def count_words(path):
    """Read a text file and return its word-frequency Counter, or None if missing."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Make sure the text file is in the project folder, or check the file path.")
        return None
    except OSError as error:
        print(f"Could not read the file: {error}")
        return None

    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_text.split()
    return Counter(words)


def show_word_count():
    """Ask for a text file and display its word statistics."""
    print("\n===== WORD COUNTER =====")
    print("A sample file named sample.txt is included in this project.")
    path = input("Enter a text file path (press Enter to use sample.txt): ").strip()
    if not path:
        path = "sample.txt"

    counts = count_words(path)

    if counts is None:
        return

    total_words = sum(counts.values())
    unique_words = len(counts)

    print("\n----- WORD COUNT RESULTS -----")
    print(f"Total words : {total_words}")
    print(f"Unique words: {unique_words}")

    if not counts:
        print("\nThe file is empty or does not contain any words.")
        return

    print("\nTop 10 most common words:")
    print(f"{'Word':<20}{'Count':>8}")
    print("-" * 28)

    for word, frequency in counts.most_common(10):
        print(f"{word:<20}{frequency:>8}")


def main():
    best_score = 0

    while True:
        print("\n======================================")
        print("       NUMBER GUESSING & WORD COUNTER")
        print("======================================")
        print("1. Play Number Guessing Game")
        print("2. Count Words in a Text File")
        print("3. Quit")
        print("======================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            current_score = play_guessing_game()
            if current_score > best_score:
                best_score = current_score
                print(f"New best score: {best_score}/100")
            else:
                print(f"Best score so far: {best_score}/100")

            replay = input("\nWould you like to play again? (y/n): ").strip().lower()
            if replay == "y":
                continue

        elif choice == "2":
            show_word_count()

        elif choice == "3":
            print(f"\nThanks for using the project! Your best score was {best_score}/100.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

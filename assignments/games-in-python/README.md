
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python by practicing string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Build the Core Game Loop

#### Description
Create a text-based Hangman game where a player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words
- Display the hidden word as underscores, such as `_ _ _ _ _`
- Ask the user to enter one letter at a time
- Reveal correctly guessed letters in the word
- Track and display the number of incorrect guesses remaining

### 🛠️ Add Win/Lose Logic and Feedback

#### Description
Finish the game by checking whether the player has guessed the word or used all available attempts, and provide clear end-of-game feedback.

#### Requirements
Completed program should:

- End the game when the player correctly guesses the whole word
- End the game when the player runs out of attempts
- Show a win message when the word is guessed correctly
- Show a lose message when the player runs out of guesses
- Keep prompting for valid input until the game ends

```python
# Example output
Word: _ _ a _ _
Guess a letter: a
Correct! You have 5 attempts left.
```
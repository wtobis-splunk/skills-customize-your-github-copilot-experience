

# 🎮 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and user input. You will learn how to manage game state and interact with users through the console.

## 📝 Tasks

### 🛠️	Create the Hangman Game

#### Description
Develop a Hangman game where the player tries to guess a hidden word by suggesting letters within a limited number of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the user and display current progress (e.g., `_ a _ _ m a n`)
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts run out
- Show a win message if the player guesses the word, or a lose message if they run out of attempts

**Example:**
```python
Word: _ a _ _ m a n
Guesses left: 3
Guess a letter: g
Word: g a _ _ m a n
Guesses left: 3
...
```

### 🛠️	Enhance User Experience

#### Description
Add features to make the game more engaging and user-friendly.

#### Requirements
Completed program should:

- Prevent repeated guesses of the same letter
- Display all guessed letters so far
- Handle invalid input gracefully (e.g., non-letter characters)

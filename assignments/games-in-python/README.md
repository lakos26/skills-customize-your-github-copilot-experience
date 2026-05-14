# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python where a player guesses letters to reveal a hidden word. You will practice strings, loops, conditionals, random selection, and handling user input.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description

Create the word list and initialize the game state before the player starts guessing.

#### Requirements

Completed program should:

- Randomly select a word from a predefined list.
- Set up the number of allowed incorrect guesses.
- Display the hidden word as underscores before any guesses are made.

### 🛠️ Letter Guessing and Progress Display

#### Description

Accept letter guesses from the player and update the displayed progress after each valid guess.

#### Requirements

Completed program should:

- Prompt the player to enter one letter at a time.
- Show the current word progress in underscore format after each guess.
- Reveal correctly guessed letters in their proper positions.
- Prevent the game from crashing when the player enters an invalid guess.

### 🛠️ Win and Lose Conditions

#### Description

Detect when the game is complete and show the appropriate ending message.

#### Requirements

Completed program should:

- Track incorrect guesses remaining.
- End the game when the word is fully guessed.
- End the game when attempts run out.
- Display a clear win or lose message at the end.

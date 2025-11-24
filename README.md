# Hangman-game
Hangman Game (Fruit Edition)
A classic, text-based implementation of the popular word-guessing game "Hangman," built using Python. This program tests your vocabulary by challenging you to guess the name of a fruit within a limited number of attempts.<br/>
<br>
Features
Interactive Interface: Includes a loading animation and timed delays for a smooth user experience.
Randomized Gameplay: Selects a random word from a predefined list of fruits every time you play.
Status Tracking: Displays the current state of the word (revealing correct guesses and keeping others hidden with _).
Input Validation: Prevents users from wasting turns by checking if a letter has already been guessed.
Smart Hint System: Automatically provides a clue (the starting letter) when the player is down to their last 2 attempts.
Win/Loss Logic: Clearly tracks the remaining turns and declares a winner or loser.
Prerequisites<br/>
<br>
Python 3.x installed on your system.
Standard libraries used: time, random (No external installation required).<br/>
<br>
How to Play
The game will load and ask for your name.
You will be presented with a hidden word represented by underscores (e.g., _ _ _ _ _).
Type a single letter and press Enter.
Correct Guess: The letter is revealed in its correct position.
Wrong Guess: You lose 1 attempt.
You have a total of 5 attempts.
If you reach 2 attempts left, the game will give you a hint (the first letter of the word).
Code Structure<br/>
<br>
Imports: Uses random to pick a word and time to add pauses for readability.
Word Bank: Currently contains: ['apple', 'mango', 'banana', 'orange', 'kiwi', 'strawberry'].
Main Loop: Runs as long as turns > 0. It checks the user's input against the selected word and updates the display variables.
Future Improvements<br/>
Category Selection: Allow the user to choose between Fruits, Animals, or Movies.
ASCII Art: Add visual drawings of the "Hangman" stick figure that build up with every wrong guess.
Replay Feature: Add a "Play Again?" loop so the user doesn't have to restart the program manually.
Author: [Jainam Jain]
Reg No [25BAI11474]


# Wordle
![image](https://user-images.githubusercontent.com/69359897/204119395-607f0316-58b2-4775-b44c-2b255f72828b.png)
*A Python implementation of Wordle that can be played via the terminal.*
## How to Play
- The user has to guess the 'Wordle' in six attempts or less.
- Each guess must be a valid 5-letter word.
- The color of the tiles will change to show how close the user's guess was to the word.
- If a letter is in the word and in the correct spot, the letter will turn green.
- If a letter is in the word but in the wrong spot, the letter will turn yellow.
- If the letter is not in the word in any spot, the letter will turn grey.
## Example
In command line, run the following `$ python3 wordle.py`.
The program will ask you to enter a five word guess.
The following is an example output: 

![image](https://user-images.githubusercontent.com/69359897/204118959-3f30dffd-ecd2-4939-aaad-3a4bac9a6069.png)

A new 'Wordle' is randomly generated each game.
## About
- The Python termcolor library provides ANSI color formatting for the letters in the terminal.
- A random word API is used to generate a new 'Wordle' each game.
- A dictionary API is used to validate each guess by the user.

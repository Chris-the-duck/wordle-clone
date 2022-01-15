# wordle-clone
An attempt at replicating the popular Wordle game in Python

I am attempting to emulate the popular game Wordle (https://www.powerlanguage.co.uk/wordle/)
in Python, entirely for purposes of my own personal learning.
(Though in my version obviously you can play as much as you want rather than once per day.)

I am using the Oxford Dictionaries API to validate words and will eventually hook it up
to a mySQL database to enable results tracking by username.

The word list is currently one I was given for doing something similar in a Python
course. If I ever actually do anything with it besides play around for my own
amusement, I will find an open source alternative.

What currently works:
- Pulling 5-letter words from the list, then picking one at random and validating it
against the Oxford API (as that list has some dodgy stuff in it that made me angry
when I was making a hangman game with it)
- Function to check the user guess against the picked word and print it out with
the letters colour coded based on whether they're correct (green), present but in
the wrong place (yellow), or not in the word at all (red)

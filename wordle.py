import requests, json, random

# Oxford dictionary API info

app_id = "01c7385d"
app_key = "7a4831c2f38ea989b124122b31993b3b"
language = "en-us"

# Getting 5 letter words from a list I happen to have

words = open("words.txt")
line = words.readline()
wordlist = []
for word in line.split():
    if len(word) == 5:
        wordlist.append(word)

# Function to check if the word is in the Oxford because some of em are bullshit
# Returns status code - if 404, the word isn't in there. If 200, it's fine.

def check_word(word):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    return r.status_code

# For formatting letter output

green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
red = "\033[1;31;40m"

# Function to actually determine a word

def find_word():
    idx = random.randrange(0, len(wordlist))
    word = wordlist[idx]
    if check_word(word) != 200:
        print("Word {} was chosen but discarded as not in the dictionary".format(word))
        wordlist.remove(word)
        find_word()
    return word

# Function to display word and available letters_guessed

def display_game(word):
    pass


# Function to take in a guess

def take_guess():
    guess = input("Guess the 5-letter word!\nNo inflections/plurals.\n").lower()
    if len(guess) != 5:
        print("FIVE. FIVE LETTERS. Surely you can count?\n")
        take_guess()
    if check_word(guess) == 404:
        print("That word isn't in the dictionary.\nRemember, no inflections/plurals.\n")
        take_guess()
    return guess

# Checking a guess against the word
guessed_right = []
guessed_halfright = []
guessed_wrong = []

def check_guess(word, guess):
    print("word:", word)
    print("guess:", guess)
    if word == guess:
        print("OMG YOU WIN")
        return
    string = ""
    for i in range(len(guess)):
        if guess[i] not in word:
            guessed_wrong.append(guess[i])
            string += red + guess[i].upper()
        elif guess[i] == word[i]:
            guessed_right.append(guess[i])
            string += green + guess[i].upper()
        else:
            guessed_halfright.append(guess[i])
            string += yellow + guess[i].upper()
    print(string)


# Main program body

print("***WELCOME TO CHRISTINA'S WORDLE RIPOFF IN PYTHON***\n\n")
#username = input("What is your name?\n")
# put option to play game vs view stats here
word = find_word()
guess = take_guess()
check_guess(word, guess)

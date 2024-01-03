# Problem Set 2, wordle.py
# Name: Tyler Proctor
# Collaborators:
# Time spent: 4 1/2 hours

# Wordle Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def check_word_list(user_guess, wordlist):
    """

    :param user_guess, a string, the user guess
    :param wordlist, a list, the list of words possible

    Returns bool for whether the user_guess is a word within the wordlist
    """
    counter = 0
    for i in range(len(wordlist)):
        if str.lower(user_guess) == (wordlist[i]):
            counter += 1
    if (counter > 0):
        return True
    else:
        return False
    

def check_user_input(secret_word, user_guess):
    """

    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, the users guess
    :return: False if user_guess does not satisfy at least
	     one of the below conditions, True otherwise.
    1. must consist of only letters (uppercase or lowercase)
    2. must be the same length as secret_word
    3. must be a word found in words.txt
    """
    global remaining_warnings
    if (len(user_guess) != len(secret_word)):
        print("Oops! That word length is not correct.")
        return False
    elif (str.isalpha(user_guess) == False ):
        print("Oops! That is not a valid word.")
        return False
    elif (check_word_list(user_guess, wordlist) == False):
        print("Oops! That is not a real word.")
        return False 
    else:
        return True

def check_if_correct(secret_word, user_guess):
    """
    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, a valid user guess
    Returns bool for if the user guessed the right word
    """
    if (user_guess == secret_word):
        return True
    else:
        return False

def check_characters_secret_word(secret_word, user_guess_char):
    """
    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, a valid user guess
    Returns bool for if the character passed appears at all in the secret word
    """
    counter = 0
    for i in range(len(secret_word)):
        if user_guess_char == secret_word[i]:
            counter += 1

    if (counter > 0):
        return True
    else: 
        return False


def get_guessed_feedback(secret_word, user_guess):
    """

    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, a valid user guess
    :param feedback: a string, the most recent show of feedback for the user
    :return: a string with uppercase and lowercase letters and 
	     underscores, each separated by a space (e.g. 'B _ _ S u')
    """
    feedback = ""
    for i in range(len(user_guess)):
        if user_guess[i] == secret_word[i]:
            feedback = feedback + " " + str.upper(user_guess[i])
        elif (check_characters_secret_word(secret_word, user_guess[i]) == True):
            feedback = feedback + " " + str.lower(user_guess[i])
        else: 
            feedback = feedback + " _"
    feedback = str.strip(feedback)
    return(feedback)



def get_alphabet_hint(secret_word, all_guesses):
    """
    takes in the secret word and a list of all previous guesses and returns a string of hint text
    :param secret_word: a string, the word to be guessed
    :param all_guesses: a list of all the previous valid guesses the user inputed
    :return: a string which replaces letters that were incorrect guesses with underscores and puts
	     semi-correct guesses (correct letter, incorrect place) in /x/
    """
    # we have coded this for you
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out_list = []
    for char in alphabet:
        out_list.append(" "+char+" ")

    for guess in all_guesses:
        for i, char in enumerate(list(guess)):
            if char not in secret_word:
                out_list[alphabet.find(char)]=" _ "
            elif char != secret_word[i]:
                out_list[alphabet.find(char)] = "/"+char+"/"
            elif char == secret_word[i]:
                if secret_word.count(char) > guess.count(char):
                    out_list[alphabet.find(char)] = "/" + char + "/"
                else:
                    out_list[alphabet.find(char)] = "|" + char.upper() + "|"
    return "".join(out_list)

def wordle(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Wordle.
    
    * At the start of the game, let the user know how many letters the 
      secret_word contains and how many guesses and warnings they start with.
      
    * The user should start with 6 guesses and 3 warnings

    * Before each round, you should display to the user how many guesses
      they have left.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a valid word!
    
    * The user should receive feedback immediately after each guess about 
      whether their guess is valid, how closely it matches the secret_word,
      and the alphabet hint.

    * After each guess, you should display to the user the progression of 
      their partially guessed words so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    remaining_warnings = 3
    remaining_guesses = 6
    guessed_correctly = False
    guess_feedback = ""
    all_guesses = []
    guess_feedback_addition = ""
    counter = 0


    print(f"""Welcome to the game Wordle!""")
    print(f"""I am thinking of a word that is {len(secret_word)} letters long.""")
    print(f"""You have {remaining_warnings} warnings remaining.""")
   
    
    while(guessed_correctly != True and remaining_guesses > 0):
        print(f"""You have {remaining_guesses} guesses left.""")
        user_guess = input("Please guess a word: ")
        if (check_user_input(secret_word, user_guess) == True):  
            remaining_guesses -= 1 
            all_guesses.append(user_guess)
            if (check_if_correct(secret_word, user_guess) == True):
                print(f"""Congratulations, you won!""")
                print(f"""You guessed the correct word in {6 - remaining_guesses} tries!""")
                total_score = remaining_guesses * len(set(secret_word))
                print(f"Your total score is {total_score}.")
                guessed_correctly = True
            else: 
                guess_feedback_addition = get_guessed_feedback(secret_word, user_guess)
                guess_feedback = guess_feedback + guess_feedback_addition + "\n"
                alphabet_hint = get_alphabet_hint(secret_word, all_guesses)
                print("WORDLE response:")
                print(guess_feedback, end="")
                print("Alphabet HINT:")
                print(alphabet_hint)
                if remaining_guesses >= 1:
                    print("--------------")
        else:
            if (remaining_warnings > 0):
                remaining_warnings -= 1
            else:
                remaining_guesses -= 1
            print(f"You have {remaining_warnings} warnings remaining.")
            print("--------------")
        counter += 1
    if (remaining_guesses == 0):
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

    
        
    

          

    # pass


if __name__ == "__main__":
    # pass

    # To test, comment out the `pass` line above and uncomment:
    # - either of the `secret_word = ...` lines below, depending on how you want to set the secret_word
    # - the `wordle(secret_word)` line to run the game

    # uncomment and change the line below to a specific word for testing
    secret_word = "none"

    # uncomment the line below for a randomly generated word
    # secret_word = choose_word(wordlist)

    wordle(secret_word)
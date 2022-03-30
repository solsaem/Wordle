
import random
from wordbank import *
from player import *

class Wordle:
    def __init__(self, wordbank):
        self.wordbank = wordbank
        self.word = self.random_word().lower()
        self.guesses = None
        self.feedback = None
        self.score = 0
        

    def random_word(self):
        random_number = random.randint(1,212)
        return self.wordbank.word_list[random_number]

    def add_guess(self, guess):
        self.guesses = guess
    
    def add_feedback(self, feedback):
        self.feedback = feedback
    
    def __str__(self):
        pass


def game(player, guesses, wordbank):
    current_game = Wordle(wordbank)
    print(current_game.word)
    for i in range(0, guesses):
        guess = input("Enter guess number: ").lower()
        is_valid = check_guess(guess)
        while is_valid == False:
            print("Guess is not valid try again")
            guess = input("Enter guess number: ").lower()
            is_valid = check_guess(guess)
        current_game.score += 1
        current_game.add_guess(guess)
        guess_feedback = check_letters(current_game, current_game.word, guess)
        current_game.add_feedback(guess_feedback)
        print(f'\n{guess} {guess_feedback}\n')
        if guess_feedback == "CCCCC":
            print(f"You found the word {current_game.word}")
            return current_game, True
    print(f"The word was {current_game.word}")
    return current_game, False


def check_letters(current_game, word ,guess):
    my_str = ""
    for i in range(0,5):
        if guess[i] == word[i]:
            my_str += "C"
        elif guess[i] in word:
            my_str += "c"
        else:
            my_str += "-"
    return my_str

def check_guess(guess):
    if len(guess) != 5:
        return False

def options():
    text = '\n p: play game \n a: add a word to bank \n g: game history \n h: highscores \n s: see word bank \n z: profiles \n q: quit game \n'
    print(text)
    option = input("Input: ")
    return option


def print_word_bank(wordbank):
    print("\nWord bank:")
    print()
    for i in wordbank.word_list:
        print(i)
    

def add_word_to_bank(word, wordbank):
    if word in wordbank.word_list:
        print("\n This word is already in the word bank!")
    elif len(word) == 5:
        wordbank.add_word(word)
        print(f"{word} added to word bank!")

    elif len(word) > 5:
        print("\nSorry! your word is too long :(")
    
    else:
        print("\nSorry! your word is too short :(")
    

def main():
    print("\nLet's play Wordle!")
    word_bank = WordBank()
    current_player = Player()

    program_running = True
    while program_running:
        choice = options()
        if choice == 'p':
            print("Playing wordle \n")
            guesses = int(input("How many guesses would you like to have?: "))
            this_game, win_or_loss = game(current_player, guesses, word_bank)
            current_player.add_game(this_game, win_or_loss)
        
        if choice == 's':
            print_word_bank(word_bank)
        
        if choice == 'a':
            print("\nAdding a word to the bank")
            word = input("\nWhat five letter word would you like to add to the word bank?: ")
            add_word_to_bank(word, word_bank)

        if choice == 'h':
            print("Highscores: \n")
            highscore = current_player.find_highscores()
            count = 0
            for i in range(len(highscore)):
                if count > 5:
                    break
                print(f"Game nr.{i+1}: {highscore[i]} guess")
                count += 1

        if choice == 'g':
            print("Game history \n")

        if choice == 'z':
            print("Profiles \n")

        if choice == 'q':
            print("See you next time!")
            program_running = False
    
    
    
    

main()
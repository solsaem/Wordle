
import random
from wordbank import *
from player import *

class Wordle:
    def __init__(self, wordbank, length):
        self.length = length
        self.wordbank = wordbank
        self.word = self.random_word().lower()
        self.guesses = []
        self.feedback = []
        self.score = 0
        

    def random_word(self):
        list_of_words_right_length = [x for x in self.wordbank.word_list if len(x) == self.length]
        random_number = random.randint(1,len(list_of_words_right_length))
        return list_of_words_right_length[random_number]

    def add_guess(self, guess):
        self.guesses.append(guess)
    
    def add_feedback(self, feedback):
        self.feedback.append(feedback)
    
    def __str__(self):
        pass


def game(player, guesses, wordbank, length):
    current_game = Wordle(wordbank,length)
    print(current_game.word)
    for i in range(0, guesses):
        guess = input(f"Enter guess number {i+1}: ").lower()
        is_valid = check_guess(guess, length)
        while is_valid == False:
            print("Guess is not valid try again")
            guess = input(f"Enter guess number {i+1}: ").lower()
            is_valid = check_guess(guess, length)
        current_game.score += 1
        current_game.add_guess(guess)
        guess_feedback = check_letters(current_game, current_game.word, guess, length)
        current_game.add_feedback(guess_feedback)
        print_previous(current_game)
        if guess_feedback == "C"*length:
            print(f"You found the word {current_game.word}")
            return current_game, True
    print(f"The word was {current_game.word}")
    return current_game, False

def print_previous(game):
    for i in range(len(game.guesses)):
        print(f"{game.guesses[i]} {game.feedback[i]}")


def check_letters(current_game, word ,guess, length):
    my_str = ""
    for i in range(0,length):
        if guess[i] == word[i]:
            my_str += "C"
        elif guess[i] in word:
            my_str += "c"
        else:
            my_str += "-"
    return my_str

def check_guess(guess, length):
    if len(guess) != length:
        return False

def options():
    text = '\n p: play game \n a: add a word to bank \n g: game history \n h: highscores \n s: see word bank \n z: profiles \n q: quit game \n'
    print(text)
    option = input("Input: ").lower()
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
    
def print_history(player):
    games = [x.score for x in player.highscore]
    for i in range(len(player.highscore)):
        print(f"Game nr.{i}: {games[i]} guesses")

def try_input(str):
    is_valid = True
    while is_valid:
        guesses = input(str)
        try:
            guesses = int(guesses)
            is_valid = False
        except:
            print("Please input a number")
    return int(guesses)

def main():
    print("\nLet's play Wordle!")
    word_bank = WordBank()
    current_player = Player()

    program_running = True
    while program_running:
        choice = options()
        if choice == 'p':
            print("Playing wordle \n")
            guesses = try_input("How many guesses would you like to have?: ")
            length = try_input("What length do you want the word to be?: ")
            this_game, win_or_loss = game(current_player, guesses, word_bank, length)
            current_player.add_game(this_game, win_or_loss)
        
        elif choice == 's':
            print_word_bank(word_bank)
        
        elif choice == 'a':
            print("\nAdding a word to the bank")
            word = input("\nWhat five letter word would you like to add to the word bank?: ")
            add_word_to_bank(word, word_bank)

        elif choice == 'h':
            print("Highscores: \n")
            highscore = current_player.find_highscores()
            count = 0
            for i in range(len(highscore)):
                if count > 5:
                    break
                print(f"Game nr.{i+1}: {highscore[i]} guess")
                count += 1

        elif choice == 'g':
            print("Game history \n")
            print_history(current_player)

        elif choice == 'z':
            print("Profiles \n")

        elif choice == 'q':
            print("See you next time!")
            program_running = False

        else:
            print("Please choose one one of the optios below :)")
    
    
    
    

main()
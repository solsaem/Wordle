
import random

class WordBank:
    def __init__(self):
        self.word_list = open_file()

    def add_word(self, word):
        if word not in self.word_list:
            self.word_list.append(word + '\n')


class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.played = 0
        self.highscore = []
    
    def add_game(self, game, won_or_lost):
        self.played += 1
        self.highscore.append(game)
        if won_or_lost == True:
            self.wins += 1
        else:
            self.losses += 1

    def find_highscores(self):
        max_score = [float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
        for i in self.highscore:
            for j in range(0,5):
                if i.score < max_score[j]:
                    max_score[j] = i.score
                    break
            
        return [x for x in max_score if x != float('inf')]



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


def open_file():
    #file_object = open("/Users/sol/Documents/GitHub/Wordle/PA6/word_bank.txt", 'r')
    file_object = open("/Users/halldorajohannsdottir/Documents/GitHub/Wordle/PA6/word_bank.txt", 'r')
    read_file = file_object.read()
    return read_file.split()

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
    option = input(text)
    return option


def print_word_bank(wordbank):
    print("\nWord bank:")
    print()
    for i in wordbank.word_list:
        print(i)
    

def add_word_to_bank(word, wordbank):
    if word in wordbank.word_list:
        print("\n This word is already in thw word bank!")
    elif len(word) == 5:
        wordbank.add_word(word) ### klára
    

def main():

    current_player = Player()
    word_bank = WordBank()
    print("\nLet's play Wordle!")
    
    program_running = True
    while program_running:
        choice = options()
        if choice == 'p':
            print("Playing wordle \n")
            guesses = int(input("how many guesses would you like to have?: "))
            this_game, win_or_loss = game(current_player, guesses, word_bank)
            current_player.add_game(this_game, win_or_loss)
        
        if choice == 's':
            print_word_bank(word_bank)
        
        if choice == 'a':
            print("Adding a word to the bank")
            word = input("What word would you like to add to the word bank?: ")
            add_word_to_bank(word, word_bank)

        if choice == 'h':
            print("Highscores: \n")
            print(current_player.find_highscores())

        if choice == 'g':
            print("Game history \n")

        if choice == 'z':
            print("Profiles \n")

        if choice == 'q':
            print("See you next time!")
            program_running = False
    
    
    
    

main()
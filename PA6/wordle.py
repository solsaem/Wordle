import random

class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.played = 0
        self.highscore = []

class Wordle:
    def __init__(self):
        self.word = self.random_word().lower()
        self.guesses = []
        self.feedback = []
        self.score = 0

    def random_word(self):
        file_object = open("/Users/halldorajohannsdottir/Desktop/HR 2022 vor/Gagnaskipan/PA6/word_bank.txt", 'r')
        read_file = file_object.read()
        list_of_words = read_file.split()
        random_number = random.randint(1,212)
        return list_of_words[random_number]

    def add_guess(self, guess):
        self.guesses.append(guess)
    
    def add_feedback(self, feedback):
        self.feedback.append(feedback)
    
    def __str__(self):
        pass


def game(player):
    current_game = Wordle()
    print(current_game.word)
    for i in range(0,5):
        guess = input("Enter guess number: ").lower()
        is_valid = check_guess(guess)
        while is_valid == False:
            print("Guess is not valid try again")
            guess = input("Enter guess number: ").lower()
            is_valid = check_guess(guess)
        current_game.add_guess(guess)
        guess_feedback = check_letters(current_game, current_game.word, guess)
        current_game.add_feedback(guess_feedback)
        print(f'\n{guess} {guess_feedback}\n')
        if guess_feedback == "CCCCC":
            print("You found the word")
            break


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

#test hihi
    


def check_guess(guess):
    if len(guess) != 5:
        return False


def main():
    current_player = Player()
    game(current_player)

main()

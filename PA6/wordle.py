import random

class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.played = 0
        self.highscore = []
    
    def add_game(self, game, won_or_lost):
        self.played += 1
        self.highscore.append(game.score)
        if won_or_lost == True:
            self.wins += 1
        else:
            self.losses += 1

    def find_highscores(self):
        max_score = [float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]
        for i in self.highscore:
            for j in range(0,5):
                if i < max_score[j]:
                    max_score[j] = i
                    break
            
        return [x for x in max_score if x != float('inf')]



class Wordle:
    def __init__(self):
        self.word = self.random_word().lower()
        self.guesses = None
        self.feedback = None
        self.score = 0

    def random_word(self):
        file_object = open("/Users/halldorajohannsdottir/Documents/GitHub/Wordle/PA6/word_bank.txt", 'r')
        read_file = file_object.read()
        list_of_words = read_file.split()
        random_number = random.randint(1,212)
        return list_of_words[random_number]

    def add_guess(self, guess):
        self.guesses = guess
    
    def add_feedback(self, feedback):
        self.feedback = feedback
    
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




def main():

    current_player = Player()
    this_game, win_or_loss = game(current_player)
    current_player.add_game(this_game, win_or_loss)

main()
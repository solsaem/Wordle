from wordbank import *
from player import *
from classwordle import *

#here is our implementation of the game itself
def game(player, guesses, wordbank, length):
    current_game = Wordle(wordbank,length)   #create instance of Wordle
    for i in range(0, guesses): # run the game as many times as user asks for
        guess = input(f"Enter guess number {i+1}: ").lower()
        #checking if guess is valid
        is_valid = check_guess(guess, length)
        while is_valid == False:
            print("Guess is not valid try again")
            guess = input(f"Enter guess number {i+1}: ").lower()
            is_valid = check_guess(guess, length)
        #modify classes
        current_game.score += 1
        current_game.add_guess(guess)
        guess_feedback = check_letters(current_game, current_game.word, guess, length)
        current_game.add_feedback(guess_feedback)
        
        print_previous(current_game) #print feedback

        if guess_feedback == "C"*length: #if you win
            print(f"\n You win! \n You found the word: {current_game.word}")
            return current_game, True
    #if you loose
    print(f"\n Sorry, you didn't find the word :( \n The word was {current_game.word}")
    return current_game, False

def print_previous(game):
    for i in range(len(game.guesses)):
        print(f"{game.guesses[i]} {game.feedback[i]}")


#create our feedback
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

#is guess right length
def check_guess(guess, length):
    if len(guess) != length:
        return False

def options():
    text = '\n p: play game \n a: add a word to bank \n g: game history \n h: highscores \n s: see word bank \n q: quit game \n'
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
    elif len(word) < 4:
        print("\nSorry! your word is too short :(")

    elif len(word) > 10:
        print("\nSorry! your word is too long :(")
    
    else:
        wordbank.add_word(word)
        print(f"{word} added to word bank!")
        
    
def print_history(player):
    games = [x.score for x in player.highscore]
    print(f" {player.played} Games played\n {player.wins} Games won\n {player.losses} Games lost \n")
    for i in range(len(player.highscore)):
        print(f" Game nr.{i+1} \n ~~~~~~~~~ \n time: {player.highscore[i].time} \n date: {player.highscore[i].date} \n number of guesses: {games[i]} \n")


# checks if nr of guesses is valid
def try_guesses_input(str):
    is_valid = True
    while is_valid:
        guesses = input(str)
        try:
            guesses = int(guesses)
            is_valid = False
        except:
            print("Please input a number")
    return int(guesses)

#is length of word valid
def try_length_input(str):
    is_valid = True
    while is_valid:
        length = input(str)
        try:
            length = int(length)
            if length >= 4 and length <= 10:
                is_valid = False
            else:
                print("Please pick a lenght of word between 4-10")
        except:
            print("Please input a number")
    return int(length)
    
    
def display_highscore(player):
    highscore = player.find_highscores()
    count = 0
    for i in range(len(highscore)):
        if count > 5:
            break
        print(f" {i+1}.place: \n ~~~~~~~~~ \n number of guesses: {highscore[i]} \n time: {player.highscore[i].time} \n date: {player.highscore[i].date} \n")
        count += 1

#Main program
def main():
    print("\nLet's play Wordle!")
    word_bank = WordBank()
    current_player = Player()

    program_running = True
    while program_running:
        choice = options()
        if choice == 'p':
            print("\nPlaying wordle! \n")
            guesses = try_guesses_input("How many guesses would you like to have?: ")
            length = try_length_input("What length do you want the word to be? (length 4-10): ")
            this_game, win_or_loss = game(current_player, guesses, word_bank, length)
            current_player.add_game(this_game, win_or_loss)
        
        elif choice == 's':
            print_word_bank(word_bank)
        
        elif choice == 'a':
            print("\nAdding a word to the bank")
            word = input("\nWhat word would you like to add to the word bank?: ")
            add_word_to_bank(word, word_bank)

        elif choice == 'h':
            print("\nHighscores: \n")
            
            display_highscore(current_player)
            

        elif choice == 'g':
            print("\nGame history \n")
            print_history(current_player)

        elif choice == 'q':
            print("Thank you for playing! See you next time :)")
            program_running = False

        else:
            print("Please choose one of the options below :)")
    
    
main()

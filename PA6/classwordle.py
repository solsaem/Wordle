import random
from datetime import *


class Wordle:
    def __init__(self, wordbank, length):
        self.length = length
        self.wordbank = wordbank
        self.word = self.random_word().lower()
        self.guesses = []
        self.feedback = []
        self.score = 0
        self.date = date.today()
        self.time = get_time()




    def random_word(self):
        list_of_words_right_length = [x for x in self.wordbank.word_list if len(x) == self.length]
        random_number = random.randint(1,len(list_of_words_right_length))
        return list_of_words_right_length[random_number]

    def add_guess(self, guess):
        self.guesses.append(guess)
    
    def add_feedback(self, feedback):
        self.feedback.append(feedback)
    

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time
    
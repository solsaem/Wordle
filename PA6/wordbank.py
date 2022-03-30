
class WordBank:
    def __init__(self):
        self.word_list = open_file() 

    def add_word(self, word):
        if word not in self.word_list:
            self.word_list.append(word)

def open_file():
    #Reyndum allt til að það þurfi ekki að setja inn input :((( we are sorry
    file = input("Please write your filepath to word_bank.txt ")
    file_object = open(file, 'r')
    read_file = file_object.read()
    return read_file.split()
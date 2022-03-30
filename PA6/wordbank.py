class WordBank:
    def __init__(self):
        self.word_list = open_file()

    def add_word(self, word):
        if word not in self.word_list:
            self.word_list.append(word + '\n')

def open_file():
    file_object = open("/Users/sol/Documents/GitHub/Wordle/PA6/word_bank.txt", 'r')
    #file_object = open("/Users/halldorajohannsdottir/Documents/GitHub/Wordle/PA6/word_bank.txt", 'r')
    read_file = file_object.read()
    return read_file.split()
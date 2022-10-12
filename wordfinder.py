import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""


    def __init__(self, filepath):
        """ Initializes file. Takes in filepath and reads the file, parses
        words in file to a new list."""
        self.words_list = []
        self.file_data = open(filepath, "r")
        self.read_file()



    def read_file(self):
        """ reads text from supplied filepath. generates word list and appends
        to instance. prints out word list"""

        for line in self.file_data:
            if line != '\n':
                self.words_list.append(line.replace('\n', ''))

        print(f"{len(self.words_list)} words read")


    def random(self):
        """ returns a random word from the word list."""
        random_word = random.choice(self.words_list)
        return random_word


class SpecialWordFinder(WordFinder):
    """ finds random words from dictionary, and ignores blank lines or
    comments"""

    def __init__(self, filepath):
        self.read_file =  self.read_file
        super().__init__(filepath)



    def read_file(self):
        self.words_list = [word for word in self.words_list if not word.startswith('#')]
        super().read_file()





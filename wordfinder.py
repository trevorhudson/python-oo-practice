import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):

        self.filepath = filepath
        self.words_list = []
        self.read_file()


    def read_file(self):
        file_data = open(self.filepath, "r")

        for line in file_data:
            self.words_list.append(line)

        print(f"{len(self.words_list)} words read")

    def random(self):
        random_word = random.choice(self.words_list)
        return random_word.replace('\n', '')





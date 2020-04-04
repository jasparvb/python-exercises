"""Word Finder: finds random words from a dictionary."""

from random import choice as random_word

class WordFinder:
    """Class to find load a list of words from a file and find a random word from that list"""
    def __init__(self, file):
        self.file = file
        self.word_list = self.read_words()
        print(self.words_read())

    def __repr__(self):
        return f"<WordFinder file={self.file} number-of-words={len(self.word_list)}>"

    def read_words(self):
        """Read the words from the file"""
        file = open(self.file, 'r')
        return [line[:-1] for line in file]

    def words_read(self):
        """Print the number of words read"""
        return f"{len(self.word_list)} words read"

    def random(self):
        """Find a random word from the word list"""
        return random_word(self.word_list)

class SpecialWordFinder(WordFinder):
    """Special word finder that removes blank lines and comments"""
    
    def words_read(self):
        """Update the word list to filter out blank lines and comments, then print number of words read"""
        self.word_list = [word for word in self.word_list if word and not word.startswith('#')]
        return f"{len(self.word_list)} words read"

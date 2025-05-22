import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    def __init__ (self, filename = "sowpods.txt"):
        with open (os.path.join(dir_path, filename), "r", encoding = 'utf-8') as sent:
            words = sent.read()
        self.listwords = re.split("\n", words)
    
    def is_valid_word(self, word):
        self.word = word
        p = input ("Type the word in upper case: ")
        if p.upper() in self.listwords:
            return ("The word is valid.")
        else: 
            return ("The word doesn't exist or it's not a word.")

    def get_anagrams(self, word):
        self.word = word
        sorted_word = sorted(word)
        anagrams = [w for w in self.listwords if sorted(w) == sorted_word and w != word]
        return anagrams

    

x = AnagramChecker()
x.is_valid_word(0)
x.get_anagrams("Reliq")

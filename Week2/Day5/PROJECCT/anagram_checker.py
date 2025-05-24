import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:
    def __init__(self, file_path = "sowpods.txt"):
        with open (os.path.join(dir_path, file_path), "r", encoding = 'utf-8') as f:
            self.word_list = [word.strip().lower() for word in f.readlines()]
    
    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w)]

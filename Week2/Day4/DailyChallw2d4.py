import re
import string

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else f"The word '{word}' was not found."

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        if not frequency:
            return None
        return max(frequency, key=frequency.get)

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)

class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "and", "the", "is", "are", "in", "at", "on", "for", "with", "to", "from", "that", "this", "of"
        }
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned_text

text = Text("I love how the grass smells under the rain. The rain is good, but the sun is better.")
print(text.word_frequency(" "))      
print(text.most_common_word())          
print(text.unique_words())   

mod = TextModification ("I love how the grass smells under the rain! The rain is good, but the sun is better.")
print(mod.remove_punctuation())          
print(mod.remove_special_characters())   
print(mod.remove_stop_words())   
import random 

class Card():
    def __init__ (self, suit, value):
        self.suit = suit 
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck():
    def __init__(self):
        suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card (s, v) for s in suit for v in value]
    
    def shuffle(self):
        random.shuffle (self.cards)
   
    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "No more cards"

x = Deck()
x.shuffle()
print(x.deal())


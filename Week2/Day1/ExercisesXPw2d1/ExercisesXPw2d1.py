# exercise 1
class Cat():
    def __init__ (self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Lisa", 12)
cat2 = Cat ("Jenna", 6)
cat3 = Cat ("Lexi", 7)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

oldest_cat = find_oldest_cat (cat1, cat2, cat3)     
print (f"The oldest is {oldest_cat.name} and is {oldest_cat.age} years old.")

#exercise 2

class Dog ():
    def __init__ (self, name, height):
        self.name = name
        self.height = height
        pass
    def bark (self):
        print (f"{self.name} goes woof!")
    def jump(self):
        x = self.height * 2
        print (f"{self.name} jumps {x} cm high!")
    def jump_height(self):
        return self.height * 2
        

davids_dog = Dog("Jessy", 120)
sarahs_dog = Dog ("Rex", 103)
dogs = [davids_dog, sarahs_dog]
        
for dog in dogs:
    print (f"The dog is {dog.name} and the height is {dog.height}")
    (dog.bark())
    (dog.jump())

if davids_dog.jump_height() > sarahs_dog.jump_height():
    print (f"{davids_dog.name} jumps higher than {sarahs_dog.name}! The jump is {davids_dog.jump_height()}")
    if sarahs_dog.jump_height() > davids_dog.jump_height ():
        print (f"{sarahs_dog.name} jumps higher than {davids_dog.name}! The jump is {sarahs_dog.jump_height()}")
    else:
        None

#exercise 3

class Song ():
    def __init__ (self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song (self):
                print (*self.lyrics, sep = "\n")
                return
pledging_my_love = Song (["Just promise me darling", "Your love in return", "May this fire in my soul, dear", "Forever burn"])
pledging_my_love.sing_me_a_song()

#exercise 4

class Zoo ():
    def __init__ (self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.grouped = {}
    def add_animal (self, new_animal):
            self.animals.append(new_animal)
    def get_animals (self):
            for i in self.animals:
                print (f"{i} is currently in the zoo.")
    def sell_animal (self, animal_sold):
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped:
                   self.grouped [first_letter] = []
            self.grouped[first_letter].append(animal)
                   
    def get_groups(self):
            for keys, values in self.grouped.items():
                 print(f"{keys} : {values}")

zoo = Zoo("Our friends")
zoo.add_animal("Giraffe")
zoo.add_animal("Bear")
zoo.add_animal("Wolf")
zoo.add_animal("Lion")
zoo.add_animal("Baboon")
zoo.add_animal ("Fox")
zoo.sell_animal("Lion")
zoo.get_animals ()
zoo.sort_animals()
zoo.get_groups ()

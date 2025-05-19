#exercise 3

import random

class Dog():
    def __init__ (self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight 

    def bark (self):
        return f"{self.name} is barking!"
    
    def run_speed (self):
        speed = self.weight/self.age * 10 
        return speed 
    
class PetDog(Dog):
    def __init__ (self, name, age, weight, trained = False):
        super().__init__ (name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True
    def play (self, *args):
        print (f"{', '.join([str(item.name) for item in args])} all play together")
    def do_a_trick(self):
        x = random.choice(tricks)
        print (f"{self.name} {x}")
    
dog4 = PetDog ("Lilo", 2, False)
dog5 = PetDog ("Sasha", 4, True)
dog6 = PetDog ("Jerry", 6, True)
tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]

dog4.do_a_trick()
dog5.do_a_trick()
dog4.play(dog4, dog5, dog6)

#exercise 4


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"{member.first_name}, Age: {member.age}")

if __name__ == "__main__":
    my_family = Family("Smith")
    my_family.born("Alice", 17)
    my_family.born("Bob", 20)

    my_family.check_majority("Alice")
    my_family.check_majority("Bob")
    my_family.family_presentation()

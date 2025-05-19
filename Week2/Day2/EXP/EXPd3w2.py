#exercise 1

class Pets():
    def __init__ (self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print (f"The {animal.name} is walking!")

class Cat(Pets):
    def __init__ (self, name, age):
        self.name = name
        self.age = age

class Bengal (Cat):
    pass

class Chartreux (Cat):
    pass

class Siamese (Cat):
    pass

bengal_obj = Bengal ("Lisa", 3)
chartreux_obj = Chartreux("Moti", 5)
siamese_obj = Siamese("Jenna", 4)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)

sara_pets.walk()

#exercise 2
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
    
    def get_power(self):
        x = self.run_speed()
        return x

    def fight(self, other_dog):
        my_power = self.get_power()
        other_power = other_dog.get_power()
        if my_power > other_power:
            return f"The strongest is {self.name}"
        elif other_power > my_power:
            return f"The strongest is {other_dog.name}"
        else:
            return f"It's a tie!"

dog1 = Dog ("Jeremy", 10, 35)
dog2 = Dog ("Amy", 5, 40)
dog3 = Dog ("Rex", 3, 15)

print (dog1.bark())
print (dog2.run_speed())
print (dog1.run_speed())

print(dog1.fight(dog2))
print (dog2.fight(dog1))
print (dog3.fight(dog1))
print (dog3.fight(dog2))

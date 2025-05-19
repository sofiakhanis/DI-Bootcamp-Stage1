class Parent():
    def __init__ (self, name):
        self.name = name

    def speak(self):
        print (f"{self.name} is speaking")

class Child(Parent):
    pass

class Grandchild (Child):
    pass

obj0 = Parent ("Sydney")
obj0.speak() #calls the function def (speak) in the class. w\o will be nothing

obj1 = Child ("Jessy") 
obj1.speak()

obj2 = Grandchild ("Dira")
obj2.speak() 


#print sounds that certain animals do with class inheritance 
class Animal(): #все что в этом классе - для всей программы
    def __init__ (self, name, age, sound, legs):
        self.name = name
        self.age = age
        self.sound = sound
        self.legs = legs

    def make_sound(self):
        print (f"{self.name} is making a {self.sound}")

class Dog(Animal):
    def __init__ (self, name, age, sound, legs, trained):
        super().__init__(name, age, sound, legs)
        self.trained = trained
    def bark(self):
        print(f'A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping - from the Dog class'

jim = Dog ("Jim", 2, "bark", 4, True)
print (jim.bark())


class Cat (Animal):
    def __init__ (self, name, age, sound, legs, trained, nickname): #merging arguments with other arguments
        super ().__init__(name, age, sound, legs)
        self.trained = trained
        self.nickname = nickname

    def get_crazy(self):
        print (f"{self.name} is running with its {self.legs} legs in full power.")

class Alien ():
    def __init__ (self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet
        
    def fly(self):
        return f'{self.name} is flying around'
    
    def sleep(self):
        return f'{self.name} is sleeping form Alien class'
    
    def make_sounds(self):
        return f'{self.name} is making a sound from {self.planet}'
    
class AlienDog (Dog, Alien): #merging classes
    def __init__ (self, name, age, sound, legs, trained, personal_name, planet): 
        Dog.__init__(self, name, age, sound, legs, trained)
        Alien.__init__(self, personal_name, planet)

dog1 = AlienDog ("Rex", 10, "WOOF", 4, True, "Rexy", "Naboo")
print(dog1.make_sounds()) #if put return in the method
print(dog1.sleep())
print(dog1.fly()) 

rex = Dog ("Rex", 13, "WOOF", 4, True) #"rex" here == "self"
linda = Cat ("Linda", 5, "meow", 4, "Trained", "Lily")

#rex.make_sound()
#linda.make_sound()
linda.get_crazy()

#exercise 

#ВАЖНО РАСПОЛОЖЕНИЕ МЕТОДА! ЕСЛИ СДЕЛАТЬ ЕГО В РОДИТЕЛЬСКОМ КЛАССЕ, ТО ЛЮБЫЕ АРГУМЕНТЫ 
#МОГУТ ИМ ВОСПОЛЬЗОВАТЬСЯ. ЗДЕСЬ get_crazy() ТОЛЬКО ДЛЯ КЛАССА КОТ

# add two other attributes specifically to the Dog class: trained (boolean), age (int)
# user the super().__init__() to do so
# create an instance of Dog after that and analyse what changed

#Try and Except

hello = "Hello"

if hello == "Hello":
    print ("Hi")

def player_input (current_input):
    valid = False
    while not valid:
        position = input('enter position 1-9: ')

class Dog():
    def __init__(self, name, color, breed, age):
        print ("Creating object")
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        pass

    #to create a method of the class

    def bark (self):
        print (f"{self.name} is barking")

    def walk(self):
        print (f"{self.name} is walking")

sheltered_dog = Dog("Jackie", "Black", "No breed", 13)
pitbul = Dog ("Lena", "White", "Breed", 10)
husky = Dog ("Rex", "Black and White", "Breed", 2)
print (pitbul.__dict__)
print(pitbul.bark())
print (husky.walk())


my_dogs = [sheltered_dog, husky, pitbul]

for dog in my_dogs:
    print (dog.breed)

#my_dogs_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]
#print (my_dogs_objects) 
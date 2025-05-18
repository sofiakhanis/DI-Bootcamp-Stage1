my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = sum(my_list)

counter = 0
for num in my_list:
    counter = counter + num

print (counter)

#map (makes the code neat, needs list to show real result)

dict = {"names" : ["Jessica", "Lily", "Irene"],
        "ages" : [25, 33, 15]}

def function1(item):
    for i in dict["names"]:
        return item.upper()
x = list(map(function1, dict["names"]))
for c in x:
    print (c) 

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


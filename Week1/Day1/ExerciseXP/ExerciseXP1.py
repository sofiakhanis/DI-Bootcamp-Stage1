#exercise 1
print ("Hello world \n"*4) 

#exercise 2
print((99^3)*8)

#exercise 3
5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #TypeError
"Hello" == "hello" #False

#exercise 4
computer_brand = "Mac"
print (f"I have a {computer_brand} computer.")

#exercise 5
name = "Sofia"
age = 25
shoe_size = 40
info = f"My name is {name}, I am {age} years old. My shoe size is {40}."
print (info)

#exercise 6
a = 8
b = 4
if a > b:
    print ("Hello World")

#exercise 7
number = int(input("Type a number: "))
if number % 2 == 0:
    print ("The number is even.")
else:
    print ("The number is odd.")

#exercise 8
my_name = "Sofia"
user_name = input("Write your name: ")
if user_name == my_name:
   print ("Wow! We have the same name!")
else: 
    print ("Unfortunately, we have different names...")

#exercise 9
height = int(input("What is your height in centimeters? "))
if height > 145:
    print ("You are tall enough to ride!")
else: 
    print("I'm sorry, you need to grow some more to ride!")


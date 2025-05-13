#exercise 1
flowers = ["rose", "sunflower", "tulip"]
plants = ["bush", "oak", "leaf"]
flow_plants = flowers + plants
print (flow_plants) 

#exercise 2
for i in range (1500, 2500):
    if i % 5 == 0 and i % 7 == 0:
        print (i)

#exercise 3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_ask = input("What is your name? ")
if user_ask in names:
    print (f"The index is {names.index(user_ask)}")
else:
    print ("Nothing")

#exercise 4

numb = int(input("Write a number: "))
numb1 = int(input("Write a number: "))
numb2 = int(input("Write a number: "))

greatest = max (numb, numb1, numb2)

print (f"The max is {greatest}")

#exercise 5

alphab = "abcdefghijklmnopqrstuvwxyz"
for let in alphab:
    if let in "aeiouy":
        print (f"{let} is a vowel. ")
    else:
        print (f"{let} is a consonant. ")

    
#exercise 6

w = input ("Write 7 words with spaces between them: ").split()
words = list(w)
letter = input("Write a character: ")
for one in words:
    if letter in one:
        print (f"The index is {one.index(letter)}")
    else:
        print (f"The letter {letter} is not here!")

#exercise 7

x = range (1, 1000001)
xs = list(x)
print (max(xs))
print (min (xs))
print (sum (xs))

#exercise 8

ver = input("Write a number: ").split(", ")
re = list(ver)
rt = tuple(ver)
print(re, rt)

#exercise 9




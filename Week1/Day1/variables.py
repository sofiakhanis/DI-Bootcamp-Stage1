#exercise 1

name = "Alice"
age = 30
city = "New York"
letter = f"Hello, {name}! You are {age} years old and live in {city}"
print(letter)

#or str.format()

print ("Hello, {}! You are {} years old and live in {}".format(name, age, city))

#exercise 2 
user_age = int(input("What is your age? "))
x = 100 - user_age
print (f"You will turn 100 in {x} years")


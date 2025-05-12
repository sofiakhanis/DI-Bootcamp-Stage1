#exercise 1

number = int(input("Choose a number: "))
length = int(input("Choose a length: "))
multiplies = [] #to fill in this list
for i in range (1, length + 1):
    multiplies.append(number * i)

print(multiplies)

#exercise 2

string_from_user = input ("Write a string: ")
result = string_from_user[0] if string_from_user else "" #check fist symbol
for char in string_from_user[1:]: #to check all other symbols
    if char != result [-1]: 
        result += char
print(result)
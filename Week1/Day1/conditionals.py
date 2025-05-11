#exercise 1
#x = input ("What is your name? ")
#y = len(x)
#if y < 5:
    #print ("You have a short name :)")

#exercise 2

num = int(input("Write one number from 1 to 100: "))
if num % 3 == 0 and num % 5 == 0:
    print ("FizzBuzz")
elif num % 3 == 0:
    print ("Fizz")
elif num % 5 == 0:
    print ("Buzz")
else:
    print (num) 
#exercise 1
print ("Hello world \n"*4 + "I love python \n"*4) 

#exersice 2
season = int(input("Write your favorite month: "))
if 3 <= season <= 5:
    print ("It's spring!")
elif 6<= season <= 8:
    print ("It's summer!")
elif 9<= season <= 11:
    print ("It's autumn!") 
elif season == 12 or season == 1 or season == 2:
    print ("It's winter!")
else:
    print ("It's not a month!")
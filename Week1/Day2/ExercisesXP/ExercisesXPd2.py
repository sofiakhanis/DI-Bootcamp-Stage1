#exercise 1
my_fav_numbers = {1, 14, 55, 32, 77, 54} 
my_fav_numbers.add (34) #adding number 
my_fav_numbers.add (45) #adding number
my_fav_numbers.remove (45) #removing number

friend_fav_numbers = {56, 18, 5, 7, 40, 58}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) #combining
print (our_fav_numbers)

#exercise 2

passwords = ("abc", "der", "wer", "abc")
temp_list = list(passwords) #make a list
temp_list.extend (["wep", "yer", "poq"]) #add passwords
passwords = tuple(temp_list) #back to tuple
print (passwords)

#exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove ("Blueberries")
basket.append ("Kiwi") #adds to the end
basket.insert (0, "Apples") 
print(basket.count ("Apples")) #output: 2
basket.clear()
print(basket)

#exercise 4

#float is a point number, integer is a whole number

int_fl = [i * 0.5 for i in range (3,11)]
print (int_fl) 

#exercise 5

numbers = range (0, 20)
for numb in numbers: #create a list of numbers
    numb += 1
    print (numb) 

other_numbers = list(range(1, 21))
for index in range(0, len(other_numbers)):
    if index % 2 == 0: #check the index
        print(other_numbers[index]) 

#exercise 6

secret_name = "Sofia"
asking_name = input ("What is your name? ")

while asking_name != secret_name: #checking the condition
    print ("Wrong name!")
    asking_name = input ("What is your name? ")             
else:
        print ("Yes, it's you!")

#exercise 7

fav_fruit = input("What are your favorite fruits? Write them separated by spaces, please (mind capitalization!): ").split() #to store fruits as words in a list
print (list(fav_fruit))
selec_fruit = input ("Type the name of any fruit you want! ")
if selec_fruit in fav_fruit:
     print ("You chose one of your favorite fruits! Enjoy!")
else:
     print ("You chose a new fruit. I hope you enjoy it!")
        

#exercise 8

toppings = [] #to edit this list
price = 10.0
topping_price = 2.50
while True:
     topping  = input ("What is your favorite pizza topping? Enter 'quit' to exit. ")
     if topping == "quit":
          break
     toppings.append (topping) #edit the list
     print (f"Adding {topping} to your pizza.")

total_cost = price + topping_price*len(toppings) #to calculate the cost
print ("\nToppings added: ")
for t in toppings:
     print(f"- {t}")
print (f"\nTotal cost: ${total_cost}")

#exercise 9

from_three_twelve = []
twelve = []
age_three_twelve = 10.0 
over_twelve = 15.0

while True:
    family_age = int(input ("What is the age of your family member? Type '-1' to calculate the total cost. "))
    if family_age == -1:
        break 
    elif family_age < -1:
        print ("Type real age, please.")
    elif 0 <= family_age < 3:
        child_age = 0
    elif 3 <= family_age <= 12:
        from_three_twelve.append (family_age)
    else:
        twelve.append (family_age) 

cost = age_three_twelve*len(from_three_twelve) + over_twelve*len(twelve)

print (f"Total cost is ${cost}.")

#bonus 
restricted_film = []

while True:
    age_of_cust = int(input("What is the age of customer? Type '-1' to calculate the cost. "))
    if age_of_cust == -1:
        break
    elif 16 <= age_of_cust <= 21:
        restricted_film.append(age_of_cust)
    else: 
        print ("You can't wantch this film.")
    
print ("Who can attend this film: ")
for age in restricted_film:
    print (f"Person aged {age}") 

#exercise 10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []

for ingr in sandwich_orders:
    if ingr == "Pastrami":
        sandwich_orders.remove("Pastrami") #to remove pastrami

for sandwich in sandwich_orders: #to create new list 
    new_sandwich = sandwich + " sandwich"
    finished_sandwiches.append(new_sandwich) 
    print (f"I made your {new_sandwich}")

print ("Finished sandwiches:")
for s in finished_sandwiches:
    print (f"- {s}")

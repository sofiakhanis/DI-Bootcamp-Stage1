#exercise 1
def display_message():
    print ("I am learning about functions in Python.")
display_message()

#exercise 2
def favorite_book(title):
    print (f"One of my favorite books is {title}.")
favorite_book ("Robin Hood")

#exercise 3
def describe_city(city, country = "Unknown"):
    print (f"{city} is in {country}")
describe_city ("Moscow", "Russia")
describe_city ("London")

#exercise 4

import random

def random_number (number):
        rand_numb = random.randint (1, 100)
        if number not in range (1, 101):
             print (f"The number is not in the range.")
        else:
             if number == rand_numb:
                  print ("success!")
             else:
                  print (f"Fail! Your number: {number}, Random number: {rand_numb}.")
random_number(55)     

#exercise 5
def make_shirt (size = "large", text = "I love Python"):
     print (f"The size of the shirt is {size}. The text is '{text}'.")
make_shirt("large")
make_shirt ("medium")
make_shirt ("small", "The weather is nice")
make_shirt(size = "small", text = "Hello!")

#exercise 6

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_magicians (magician_names):
     for magician in magician_names:
          print(magician)
show_magicians(magician_names)

def make_great (magician_names):
     for magician in magician_names:
          new = magician + " the Great"
          print (new) 
make_great(magician_names)

#exercise 7
def get_random_temp():
    return random.randint (-40, -10)

def main():
    temp = get_random_temp ()
    print (f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print ("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 < temp < 16:
        print ("Quite chilly! Don't forget your coat.")
    elif 16 <= temp <= 23:
        print ("Nice weather.") 
    elif 24 <= temp <= 32:
        print ("A bit warm, stay hydrated.")
    else:
        print ("It's really hot! Stay cool.")
        
main() 

#bonus 

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 10), 1)
    elif season == "spring":
        return round(random.uniform(5, 20), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(10, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1) 

def get_season_by_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None
    
def main():
    try:
        month = int(input("Enter the current month (1–12): "))
        season = get_season_by_month(month)
        if season is None:
            print("Invalid month. Please enter a number between 1 and 12.")
            return

        temperature = get_random_temp(season)
        print(f"\nThe temperature right now is {temperature}°C.")

        if temperature < 0:
            print("Brrr, that's freezing! Wear some extra layers today.")
        elif 0 <= temperature <= 16:
            print("Quite chilly! Don't forget your coat.")
        elif 17 <= temperature <= 23:
            print("Nice weather.")
        elif 24 <= temperature <= 32:
            print("A bit warm, stay hydrated.")
        elif 33 <= temperature <= 40:
            print("It's really hot! Stay cool.")
        else:
            print("Unexpected temperature range.")
    except ValueError:
        print("Please enter a valid number for the month.")


main()

                            
                               

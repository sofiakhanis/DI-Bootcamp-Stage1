#args - tuples

def hello (*args):
    print (f"Hello, {args}")
hello ("Rick", "Lenny") #turns the output in a tuple ("Rick", "Lenny")

def hello (language, *args):
    print (f"Hello, {language}, {args}")
hello ("Rick", "Lenny") #the first will be argument, the second goes into a tuple

def hello (*args):
    for a in args:
        print (f"Hello, {a}")
hello ("Rick", "Lenny") #with for will show arguments in different rows NOT in a tuple


#kwargs - dictionaries

def check_keyword (**kwargs):
    print (kwargs)
check_keyword (age = 12, age2 = 14) 
#returns a dictionary with keyword arguments 

def checked_kw (**kwargs):
    for k in kwargs.values():
        print (f"Hi, {k}")
checked_kw (name = "Lady", name1 = "Lord")
#to show the values of this new dictionary 

#exercise 

def tasks_manager (*args):
    for task in args:
        print (f"Today I need to do: {task}")
tasks_manager ("laundry", "cleaning")

#together

def check_solution (required_arg, *args, **kwargs):
    print (required_arg)
    if args:
        print (args)
    if kwargs:
        print (kwargs)

check_solution ("meow", 33, "play", 44, name = "Paul", surname = "Smith")
#need to write the key to tell the computer where args end! order is important
#kwargs are keyword, that's why they are in the end 

def qwer (*args, **kwargs):
    print ("*args", args)
    print ("**kwargs", kwargs)
qwer(12, 56, name = "Cecily") 

#when we print * in front of argument name, it automatically goes to tuple
#when ** - automatically in a dictionary 

def queens_behavior (*purr, **slay):
    print (f"The tuple is: {purr}")
    print (f"The dictionary is: {slay}")
    for gurl, damn in slay.items():
        print (f"Queen of rap {damn}")
queens_behavior("yass", "mama there is a DIVA behind you <3", name = "Nicki", surname = "Minaj")

#exercise 2

def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : {value}')

party_planner (["steak", "wine"], guest = "One", guest2 = "two")
party_planner ("lemonade")
party_planner (yes = "no", no = "yes")
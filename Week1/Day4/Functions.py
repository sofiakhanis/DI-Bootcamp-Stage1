#Function syntax

def func_name ():
    '''prints a phrase on the console''' #docstring to connect with function to explain it
    print ("I am a function") #nothing will be shown because you need to call the fuction
func_name() #only after calling will show!
print (func_name.__doc__) #to print docstring 

#exercise: create a function called greetings 

def greetings():
    print ("Привет")
greetings ()

#exercise

def country_info (country = "Japan"): #allows to use other arguments too!
    if country == "Japan":
        print ("The capital is Tokyo.")
    elif country == "Russia":
        print ("The capital is Moscow.")
    else:
        print ("Sorry, I don't know.")

country_info("Russia")




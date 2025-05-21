#re.findall()
import re

string = "at what time today attempted?"
match = re.findall('at', string) #returns all instances of "at" in string
print (match)
#output: ['at', 'at', 'at'

#re.search()
string1 = "hello i am doint"
match1 = re.search("int", string1)
if (match1):
    print ("String found at: ", match1.start()) #the first index of first occurrence
else:
    print ("String not found!")
#output: String found at:  13

#re.split()
string2 = "a place is hunted"
match2 = re.split("a", string2) #splits the string in a list and deletes what is chosen
print (match2)
#output: ['', ' pl', 'ce is hunted']

#re.sub()

string4 = "at what time?"
match4 = re.sub (" ", "!!!", string4) #replaces " " with !!! in all instances
print (match4)
#output: at!!!what!!!time?

import requests
import json 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get("https://api.chucknorris.io/jokes/random")
#print (response.text)

data = json.loads (response.text)

with open (f"{dir_path}/jokes.json", "w", encoding = 'utf-8') as f:
    json.dump (data, f, indent=2, sort_keys = True)

print (data["value"])

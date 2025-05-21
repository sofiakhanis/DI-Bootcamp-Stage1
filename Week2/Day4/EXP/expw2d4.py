#exercise 1

import os
import re 
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_words_from_file (filename = "words.txt"):
    with open (os.path.join(dir_path, filename), "r", encoding = 'utf-8') as sent:
        words = sent.read()
        listwords = re.split("\n", words)
        return listwords

def get_random_sentence (length):
    lists = get_words_from_file ()
    randomsent = random.choices(lists, k = length)
    sentence = ' '.join (randomsent).lower() 
    print(sentence)

def main():
    print ("The program selects random words from the list of words and creates a sentence with them.")
    len = input("What is the length of the sentence?: ")
    x = isinstance(len, int)
    if x == True or 2 <= int(len) <= 20:
        get_random_sentence(int(len))
    else:
        print ("Wrong input.")
    exit

main()

#exercise 2
import json
import os
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__)) 

json_file = "dict.json"

with open (f"{dir_path}/dict.json", 'r') as f:
    new_dict = json.load(f)
    salary = new_dict["company"]["employee"]["payable"]["salary"]
    print (salary)
    new_dict["company"]["employee"].update({"birth_date" : "2025-05-21"})
    print (new_dict)

with open (f"{dir_path}/dict.json", 'w') as f:
    json.dump(new_dict, f, indent = 2)
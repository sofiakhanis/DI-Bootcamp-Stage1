#exercise 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__ (self):
        return f"{self.amount} {self.currency}s"
    
    def __int__ (self):
        return int(self.amount)
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            return NotImplemented
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print (repr(c2))
print (c2 + 5)
print (c1 + c2)
print (c1)
c1 += 5
print (c1)
c1 += c2
print (c1)
#print(c1 + c3) #gives an error

#exercise 3

import string
import random

all_letters = string.ascii_letters
random_string = ' '
for i in range(5):
    random_char = random.choice(all_letters)
    random_string += random_char

print(random_string)

#exercise 4

import datetime

x = datetime.datetime.now()
print (x.strftime("%D"))

#exercise 5

date = datetime.datetime.now()
next = date.year + 1
s = datetime.datetime (next, 1, 1)
final_date = s - date

print (f"Time left: {final_date}")

#exercise 6

def minutes_lived (birthday):
    try:
        birthdate = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        now = datetime.datetime.now()
        time = now - birthdate 
        minutes = int(time.total_seconds() // 60)

        print (f"You have lived {minutes} minutes.")
    except ValueError:
        print ("Please, write valid date format: YYYY-MM-DD")

birthdate = input("Write your birthday (YYYY-MM-DD): ")
minutes_lived(birthdate)   

#exercise 7
#imported faker by pip install faker

from faker import Faker
user_list = []

def add_users(num):
    fake = Faker ()
    for i in range(num):
         user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
    user_list.append(user)

add_users (4)
for i, user in enumerate(user_list, 1):
    print(f"User {i}:")
    print(f"  Name: {user['name']}")
    print(f"  Address: {user['address']}")
    print(f"  Language: {user['language_code']}")
    print()




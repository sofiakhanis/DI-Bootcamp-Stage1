shopping_list = ["milk", "bread", "meat"]

dictionary = {
    "ingr1" : "milk",
    "ingr2" : "bread",
    "ingr3" : "meat"
    }

print (dictionary ["ingr1"]) #to print only one element

print (dictionary.items()) #to print all elements 

for key, value in dictionary.items ():
    print (key, "->", value)
#output: ingr1 -> milk ingr2 -> bread ingr3 -> meat

a_dict = {'color' : 'blue', 'fruit' : 'apple', 'pet' : 'dog'} 
for key, value in a_dict.items():
    print (key, "->", value)

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print (sample_dict.items())
for key, value in sample_dict.items():
    print (key, "->", value)
print (sample_dict ['class']['student']['marks']['history']) #to get to history result

shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]
for shirt in shirts:
  print(shirt['size'])


x = sample_dict.get ("class")
print(x)

sample_dict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"

}

del sample_dict ['name']
del sample_dict ['salary']
print (sample_dict.items())

for x, y in sample_dict.items():
    print ("the " + x + " is " + str(y))

print (list(range(1, 10, 2))) #to make the range a list




#FOR LOOPS 

#for <variable_name> in <sequence_name>:
    #CODE
    #CODE

fruits = ['apple', 'banana', 'kiwi', 'pear']
for fruit in fruits:
  print("I love " + fruit + "!")

for i in range (1, 10):
   print(i)

for i in range (len(fruits)):
  print (i) 

odd_nums = list (range(1, 11, 2))
print (min(odd_nums))


#WHILE LOOP

current_number = 1
while current_number <= 10:
  print(current_number)
  current_number += 1
print ("Finished")

num = 1
while num <= 10:
  if num == 5:
    break
  print (num)
  num += 1

#number guessing game 

secret_num = 7
user_num = int(input("Try a number: "))
while user_num != secret_num:
  print ("Try again!")
  user_num = int(input("Try a number: "))
if user_num == secret_num:
  print ("Congrats!") 

#MUlTIPLICATION TABLE 

bee = int(input("Write your number: "))
if 0 < bee < 11:
  for b in range (1, 11):
    print(b*bee)


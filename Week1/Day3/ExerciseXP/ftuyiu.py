users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#1
dict_1 = {}
for index, char in enumerate(users):
    dict_1 [char] = index
print (dict_1)

#2
dict_2 = {}
for ind, qwe in enumerate(users):
    for i in users:
        dict_2 [ind] = qwe
print (dict_2) 

#3

disney = sorted(users)
print (disney)

dict_3 = {}
for indx, chr in enumerate(disney):
    dict_3 [chr] = indx
print (dict_3)
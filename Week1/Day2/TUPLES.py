my_tuple = ("TLV")
print (type(my_tuple)) #it's a string!

my_tuple_real = ("TLV", )
print(type(my_tuple_real)) #it's a tuple! must be more than 1 in tuple

tup = tuple (range(11))
print (tup) #output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#METHODS

passwords = ("abc", "der", "wer", "abc")
print (passwords.count ("abc")) #shows 2, because abc happens 2 times 

#access by index
print (passwords[1]) #shows "der" 

#how to change a tuple 
#(can't change the tuple on its own! only through converting to list)
temp_list = list(passwords)
print (temp_list)
temp_list.extend (["wep", "yer", "poq"])
passwords = tuple(temp_list)
print (passwords) #will show ('abc', 'der', 'wer', 'abc', 'wep', 'yer', 'poq')










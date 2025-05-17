#LISTS

x = "item 1"
my_list = list(x)
print (my_list) # ['i', 't', 'e', 'm', ' ', '1']

#difference 
sec_list = ["item 1"]
print (sec_list) #['item 1']
print (len(my_list)) #6 
print (my_list[0]) #i 

#METHODS
my_list.append ("2") #adds one element in the end of the list
print (my_list) #['i', 't', 'e', 'm', ' ', '1', '2']

my_list.extend ([3, "C", 6]) #adds number of elements in the end of the list
print (my_list) #['i', 't', 'e', 'm', ' ', '1', '2', 3, 'C', 6]

#exercise 1
names = []
names.extend (["Jack", "Lily", "Mary", "Ron"])
print (names)

#range (start, stop, step)
print (list(range (7))) #to print all numbers from 0 to 7, firstly convert into a list!
print (range (7)) #output: range(0, 7)
print (list(range(1,8))) #output: [1, 2, 3, 4, 5, 6, 7]
print (list (range(1, 8, 2))) #output: [1, 3, 5, 7] doesn't include stop number
nums_list = list(range(1,8))
print (nums_list)
print(nums_list[2:5]) #output: [3, 4, 5]
print (nums_list[:5]) #output: [1, 2, 3, 4, 5]

#TO COPY THE LIST 
copied_list = nums_list [:] #copies the list
print(copied_list)

#OR

copied_list = nums_list.copy ()
print (copied_list) #output: [1, 2, 3, 4, 5, 6, 7]

#delete

del nums_list [3] #indexing
print (nums_list) #output: [1, 2, 3, 5, 6, 7]

#nums_list.pop()
#print(nums_list)

poped_el = nums_list.pop()
print (poped_el) #will show the element that was deleted 

#sorted() doesn't change the original list! 
list1 = ["banana", "orange", "apple"]
print (sorted(list1)) #['apple', 'banana', 'orange']
print (list1) #['banana', 'orange', 'apple']
 
#BUT

#.sort() CHANGES the original list
list1.sort()
print (list1) #['apple', 'banana', 'orange']

#index (element) - returns the index of the element 

#to find the index of '20', then change the first occurence of it to '200'
list2 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list2: #index 3
    index_found = list2.index(20)
    list2.remove(20)
    list2.insert (index_found, 200)
    print(list2)
else:
    print ("element not found") 

list_1 = [1, 2, 3]
list_2= [4, 5, 6]

list_3 = [list_1, list_2]
list_4 = [*list_1, *list_2] #combine lists

print (list_3)
print (list_4) 







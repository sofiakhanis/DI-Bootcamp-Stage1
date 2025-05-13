#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip (keys, values))
print (new_dict)

#exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

three_twelve = 10
over_twelve = 15

list_thrtw = []
list_over = []
for name, age in family.items():
        if  3 <= age <= 12:
            list_thrtw.append (age)
            print (f"The cost for {name} is ${three_twelve}")
        elif age > 12:
             list_over.append (age)
             print (f"The cost for {name} is ${over_twelve}")
        else:
            None 

total = len(list_thrtw)*three_twelve + len(list_over)*over_twelve
print (total)
    
#bonus 
name_cust = input ("What are the names of all customers? Please, type and divide the names with spaces: ").split()
age_cust = input ("What are the ages of all customers? Please, type the ages in the same order and divide them with spaces: ").split()

family_tot = dict(zip(name_cust, age_cust))

three_twelve = 10
over_twelve = 15

list_thrtw_2 = []
list_over_2 = []
for name, age in family_tot.items():
        if  3 <= int(age) <= 12:
            list_thrtw_2.append (age)
            print (f"The cost for {name} is ${three_twelve}")
        elif int(age) > 12:
             list_over_2.append (age)
             print (f"The cost for {name} is ${over_twelve}")
        else:
            None 

total = len(list_thrtw_2)*three_twelve + len(list_over_2)*over_twelve
print (total)
    

#exercise 3


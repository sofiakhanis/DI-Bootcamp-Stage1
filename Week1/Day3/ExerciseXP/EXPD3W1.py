#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip (keys, values)) #to create dictionary
print (new_dict)

#exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8} #given dictionary

three_twelve = 10 
over_twelve = 15 #prices

list_thrtw = [] #for children
list_over = [] #for adults
for name, age in family.items(): #important to include both! to check each item in dictionary
        if  3 <= age <= 12:
            list_thrtw.append (age) #to add to list
            print (f"The cost for {name} is ${three_twelve}") 
        elif age > 12:
             list_over.append (age) #to ass to list
             print (f"The cost for {name} is ${over_twelve}")
        else:
            None 

total = len(list_thrtw)*three_twelve + len(list_over)*over_twelve #calculate the coat
print (total)
    
#bonus 
name_cust = input ("What are the names of all customers? Please, type and divide the names with spaces: ").split() #ask for names and divide them in the list with split
age_cust = input ("What are the ages of all customers? Please, type the ages in the same order and divide them with spaces: ").split() #ask for ages
 
family_tot = dict(zip(name_cust, age_cust)) #create a dictionary with their input

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

brand = {
     'name': 'Zara',
     'creation_date': '1975',
     'creator_name' : 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors' : ['Gap', 'H&M', 'Benetton'],
'number_stores' : 7000,
'major_color' : {
    'France' : ['blue'],
    'Spain' : ['red'], 
    'US' : ['pink', 'green']
    }
}
 
brand['number_stores'] = 2
print (f"In Zara stores you can find clothes for {brand ["type_of_clothes"] [0]}, {brand ["type_of_clothes"] [1]}, and {brand ["type_of_clothes"][2]}. Also, there are plenty {brand ["type_of_clothes"][3]} goods.")

brand ['country_creation'] = 'Spain'

if 'international_competitors' in brand:
     brand['international_competitors'].append ("Desigual") #addition to key

del brand ['creation_date']

print (brand['international_competitors'][-1]) 

print (brand ['major_color']['US']) #to get to "US"

print (len(brand))

print (brand)


#bonus

more_on_zara = {
     'creation_date': '1975',
     'number_stores' : 7000,
}

brand.update(more_on_zara) #adding dictionary to the first dictionary 
print (brand)

#exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1
dict_1 = {}
for index, char in enumerate(users): #to get indexes and values
    dict_1 [char] = index #to ad them to dictionary 
print (dict_1)

#2
dict_2 = {}
for ind, qwe in enumerate(users): 
    for i in users:
        dict_2 [ind] = qwe
print (dict_2) 

#3

disney = sorted(users) #to sort the list without changing it permanently
print (disney)

dict_3 = {}
for indx, chr in enumerate(disney):
    dict_3 [chr] = indx
print (dict_3)
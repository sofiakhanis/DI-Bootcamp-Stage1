f = open("/Users/sofahanis/Desktop/DI_Bootcamp/Week2/Day4/secrets.txt")
secret_data = f.read()
print (secret_data) #to get the info from the document 

with open ('/Users/sofahanis/Desktop/DI_Bootcamp/Week2/Day4/secrets.txt', encoding = "utf-8") as file_obj:
    x = file_obj.read()
    x = file_obj.readlines (1)
print (x)
#certainly will close the file

from collections import Counter

names = open ("/Users/sofahanis/Desktop/DI_Bootcamp/Week2/Day4/nameslist.txt")
sect = names.read() #only first 5 chars
names.seek(0)
#names = open ("/Users/sofahanis/Desktop/DI_Bootcamp/Week2/Day4/nameslist.txt")
sect1 = list(map(str.strip, names.readlines()))
sect2 = Counter (sect1)
print(sect2 ["Darth"]) #to count Darth in the text file
print(sect1)

list_str = names.readlines ()
print (list_str)
upd = []
for line in list_str:
    print (line.split())
    if line == "Luke\n":
        upd.append("Skywalker")



#import os 

#dir_path = os.path.dirname(os.path.realpath(__file__))

#with open (f"{dir_path}/secrets.txt", "a", encoding = "utf-8") as file_obj2:
    #"a" appends and not deletes!! "w" deletes what was before
    #names = ["Jam", "Finn", "Martha"]
    #names2 = ["Jam \n", "Finn \n", "Martha \n"]
    #file_obj2.writelines("Hello there \n")
    #file_obj2.writelines("Theres id \n")
    #file_obj2.writelines (names)
#file_obj2.writelines (names2)
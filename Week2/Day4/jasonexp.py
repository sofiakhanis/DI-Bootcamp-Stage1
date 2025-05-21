import json 
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) 

my_family = {
    "parents" : ['Beth', 'Jerry'],
    "children" : ['Summer', 'Morty']
}

json_file = "my_file.json"

with open(f"{dir_path}/my_file.json)", "w") as file_object:
    json.dump(my_family, file_object) #to create a file

json_m_f = json.dumps (my_family) #to create a string 
print (json_m_f)

#to open a json file and convert into a dictionary
with open (f"{dir_path}/fam.json", 'r') as f:
    my_family2 = json.load(f)
print (my_family2)

parsed_family = json.loads(json_m_f)
print (parsed_family)
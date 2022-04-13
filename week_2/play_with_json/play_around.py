import json
# DON'T NAME MODULES/DIRECTORIES "JSON"

# JSON
# Javascript Object Notation
# Kind of like dictionaries really (not actual python dictionaries though). Key:Value pairs
'''
car = {"make": "tesla", "engine": "electric", "faults": "lots", "is_expensive": True, "driver": None}
#dumps (the s at the end stands for string!)
json_dumps = json.dumps(car)
print(json_dumps, type(json_dumps))
'''
#dumps seems to take a dictionary and "dump" it as a string
#(useful as then we can dump that string into files)

'''with open("new_car_json_file.json", "w") as jsonfile:
    #print(jsonfile, type(jsonfile))
    json.dump(car, jsonfile)'''

# API ----> Application Programme Interface
'''
LOADING FROM JSON FILE (to dictionary)
with open("new_car_json_file.json", "r") as jsonfile:
    new_car = json.load(jsonfile)

print(new_car, type(new_car))
'''

# Create dictionary, write to json file
# Create json file, read it in as dictionary

# CREATE

'''
my_dictionary = {"Sam": "Name", "Old": False}

with open("my_json_file.json", "w") as jsonfile:
    json.dump(my_dictionary, jsonfile)
'''

# LOAD

'''
with open("created_json_file.json", "r") as jsonfile:
    new_dict = json.load(jsonfile)

print(new_dict)
'''

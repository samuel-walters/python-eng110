# Key-Value Pairs

me = {"name": "Sam",
      "job": "DevOps Trainee",
      "age": 24}

# can't index based on position. dictionaries
# don't care about oder. they are about keys.

#print(me["job"])

me["job"] = "Chef"

#print(me)

me["hobbies"] = ["videogames", "chess"]
# gets the values paired with given key
#print(me.get("name"))
# update values
me.update({"name": "Samuel Walters"})
#print(me)

#difference between get and square brackets....

# try to use a key that does not exist?
#print(me["height"])
# KEY ERROR!!!

# BUT me.get("height") doesn't have the same problem.
# IT INSTEAD RETURNS None

#print(me.get("height"))

# Make a dictionary with information about your
# favourite film

the_shining = {"Director": "Stanley Kubrick", "Genre": "horror", "Rotten Tomatoes Score": 93, 
               "Release Year": 1980, "Budget": "$19 million", "Box Office": "$47.3 million",
               "Characters": ["Jack", "Wendy", "Danny"]}


the_shining["Protagonist"] = "Jack Torrance"

#print(the_shining["Characters"][0])

# METHODS FOR DICTIONARIES

#print(the_shining.keys())
#print(the_shining.values())
#print(the_shining.items())


# SETS

utensils = {"fork", "knife", "spoon", "spatula"}
print(utensils)

empty = {}

#print(type(empty))

#ASSUMES EMPTY CURLY BRACKETS IS A DICTIONARY

# initialise a set as so:

#empty = set()

#print(type(empty))

# sets are UNORDERED. which means you CANNOT index them

#print(utensils[0])
# not subscriptable... i.e. can't use square brackets (use index)

utensils.add("garlic press")
# SETS - NO DUPLICATES. 
utensils.add("spoon")
#print(utensils)

# SETS = UNORDERED UNIQUE COLLECTION
duplicate_lst = [1,2,3,4,4,4,4,4,4,4,4,4]
#print(list(set(duplicate_lst)))

utensils.remove("spoon")

#print(utensils)

# set theory... lots of different methods for sets.


# Frozen Sets - AN IMMUTABLE VERSION OF A SET. (Quite rare)

x = frozenset([1, 2, 4, 6])

print(x, type(x))
















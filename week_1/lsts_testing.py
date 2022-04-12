#shopping_list = ["eggs", "milk", "bacon", "bacon", "bananas", "chocolate", "bread"]
#print(shopping_list, type(shopping_list))
#print(shopping_list[-1])
#print(shopping_list[::2])
# breaks points (red circles) - for debugger
#shopping_list.append("cake")
#shopping_list.append("protein_powd")
#print(shopping_list)
# removes the first instance if there are multiple
# e.g. (two bacons in this list)
#shopping_list.remove("bacon")
#print(shopping_list)

#colours = ["blue", "red", "green", "purple", "yellow"]

###### methods
#h = "hello"
#print(h.upper()) # method that RETURNS something
# h won't change though. e.g. try printing h.

# but methods like append and remove CHANGES the
# item that the method is called on. 
# METHODS RETURN SOMETHING OR THEY CHANGE THE THING
# SOME DO BOTH
# e.g. .pop()

#print(colours.pop()) # what is popped
#print(colours) # the updated list as well


# with pop - by default it does it by the final value

# lists can contain all sorts of things - even
# other collections!
mixed = [True, [1, 2, 3], 3.14, "hello"]

#print(mixed)

#print(mixed[1][0])

mixed[0] = False

#print(mixed)


# TUPLES
# not going to be overwritten? use a tuple
# UNLIKE LISTS, TUPLES ARE IMMUTABLE.
# TUPLES - IMMUTABLE ORDERED COLLECTION

instruments = ("piano", "guitar", "drums", "tuba")
print(instruments, type(instruments))
print(instruments.index("piano"))
print(instruments.count("drums"))

print(instruments[0])


a = "hello world"

# indexing
# slicing
# inclusive of first index
# excludes the last index

# take every other thing from the string


# -0 is not a number. negative 0?
# -1 is a distinct number.

#print(a[-1])

#print(len(a))


# string methods

# methods - functions associated with the string class

s = "#######Engine###ering 110      "

# methods and functions both need round brackets

# useful for clearing things up
# only removes it from the end
#print(s.strip("#"))

#print(s.replace("e", "ooo"))

# method chaining

# make sure the code is still readable though...

#print(s.replace("e", "ooo").upper().replace("E", "ooo"))


# concatenation 

a = "here is "
b = 5
c = " aaaaaaa"

print(a + str(b) + c)

#print(d.capitalize() + ".")


# F-strings (formatted strings)

# much much more clean.

#to_print = f"{a} {b}"

#print(to_print)

a = input("what are you called?:\n")

print(f"You are called {a}.")

b = input("How old are you?:\n")

print(f"You are {b} years old.")
print(type(b))








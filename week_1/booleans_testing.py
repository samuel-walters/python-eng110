#bool_variable = False

#print(type(bool_variable))

#print(43 == 43)


#print(10 <= 20)

#print(10 > 5 and 10 % 2 == 0)

#print(10 > 5 or 10 < 5)

#hi = "1123434ffafa"

#print(hi.startswith("Hell"))
# should all be alphabets (no spaces)
#print(hi.isalpha())
#print(hi.islower())
# only returns true if all characters are numbers - no spaces
#print(hi.isnumeric())
# similar to isdigit()
# ^ isdigit() ---> needs everything to be a digit.
# some unicode characters are numeric, but not digits.


#print(int(True))
#print(int(False))
#print(f"1 is treated as {bool(1)}")

# only zero resolves to false 

# empty strings can be false
# ----------------------------------------------

x = None
# similar to null
print(type(x))
print(bool(x))
print(x is None)
print(x is False)




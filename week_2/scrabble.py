class Scrabble:
    def __init__(self):
        self.value_dict = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
                           "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
                           "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
                           "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
                           "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                           "Z": 10}

    def get_value_count(self, stringy):
        if stringy.isalpha() == False:
            return "Please ensure your word only has alphabet characters."
        count = 0
        for letter in stringy.upper():
            count += self.value_dict[letter]
        return count


#obj = Scrabble()
#user_input = input("Feed me a word and I will return its value\n")
#print(obj.get_value_count(user_input))

class Bank:
    def __init__(self):
        self.money = input("How much money do you have?\n")

    def __format__(self, format_spec):
        if format_spec == "m":
            return "£" + self.money[0:2] + "." + self.money[2:4]
        elif format_spec == "o":
            return "hey!"

obj = Bank()
print(f"{obj:o}")
'''
try:
    file = open("order.txt")
except FileNotFoundError as e:
    print("There has been an error:\n" + str(e))


def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()
        for line in file_line_list:
            print(line.rstrip("\n"))
        opened_file.close()
    except FileNotFoundError:
        print("File cannot be found or directory is wrong :(")
        raise
open_and_print_file("order.txt")

def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip("\n"))
    except FileNotFoundError:
        print("File cannot be found or directory is wrong :(")
        #raise
    finally:
        print("\nExecution complete")

open_and_print_file("order.txt")'''

from scrabble import Scrabble
obj = Scrabble()

def write_to_file(file):
    total_score = 0
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()
        for i in range(len(file_line_list)):
            if file_line_list[i].isdigit() == False:
                continue
            if i == len(file_line_list) - 1:
                total_score += int(file_line_list[i])
        opened_file.close()
    except FileNotFoundError:
        print("File cannot be found or directory is wrong :(")
        raise

    user_input = input("Enter a word and we'll record the score:\n")
    if user_input.isalpha() == False:
        return 
    try:
        with open(file, "a") as file:
            file.write("\nWord: " + user_input + " Score: " + str(obj.get_value_count(user_input)))
            total_score += obj.get_value_count(user_input)
            file.write("\nTotal score:")
            file.write("\n" + str(total_score))
    except FileNotFoundError:
        print("File not found")
        raise
    finally:
        ("\nExecution complete")

write_to_file("order.txt")


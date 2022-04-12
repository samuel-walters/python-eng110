import csv

with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # gets rid of the "email" bit
    iterable_csv = iter(csvreader)
    # skip the header
    next(iterable_csv)
    for row in csvreader:
        print(row[-1])

def transform_user_details(csv_file_name):
    new_user_details = []

    with open("user_details.csv", newline="") as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")
    
        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_details.append(transformation)
    return new_user_details

print(transform_user_details("user_details.csv"))


def create_new_csv(old_file, new_file):
    user_data = transform_user_details(old_file)
    new_file = open(new_file, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(user_data)

create_new_csv("user_details.csv", "new_file.csv")
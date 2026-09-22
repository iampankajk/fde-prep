# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line)

# names = []

# with open("names.txt", "r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print("Hello, ", name)

students = []

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name":name, "house":house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


import csv

# with open("names.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name":name, "home":home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} from {student['home']}")


# with open("names.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"], "home":row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} from {student['home']}")


name = input("What's your name? ")
home = input("Where is your home? ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})
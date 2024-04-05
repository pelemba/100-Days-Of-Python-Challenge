import random

name_string = input("Give me everybody\'s names seperated by a comma\n")
names = name_string.split(", ")

random_names = random.randint(0, len(names) - 1)
print(f"{names[random_names]} is paying for the meal")

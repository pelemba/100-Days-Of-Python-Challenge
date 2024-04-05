import random

name_string = input("Give me everybody\'s names seperated by a comma\n")
names = name_string.split(", ")
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " will pay for the meal")

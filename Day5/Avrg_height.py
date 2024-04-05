total_height = 0
number_of_students = 0
heights = input("Enter a list of student heights: ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])

for height in heights:
    total_height += height

for student in heights:
    number_of_students += 1
average = round(total_height / number_of_students)
print(f"The average of the students heights is {average}")


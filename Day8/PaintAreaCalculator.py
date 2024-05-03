import math
def paint_cal(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need {num_of_cans} cans of paint")
    return num_of_cans


height = int(input("Enter the height: "))
width = int(input("Enter the width: "))
cover = 5
paint_cal(height, width, cover)

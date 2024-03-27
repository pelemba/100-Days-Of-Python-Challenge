print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm: "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    want_photo = (input("Do you want a photo? Y or N: ")).upper()
    if want_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

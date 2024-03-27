print("Welcome to Pizza deliveries")
size = (input("What size pizza? S, M or L: ")).upper()
add_pepperoni = (input("Do you want to add pepperoni? Y or N: ")).upper()
extra_cheese = (input("Do you want extra cheese? Y or N: ")).upper()

bill = 0
if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")

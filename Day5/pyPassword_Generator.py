# password generator
import random
password_list = []
password = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '%', '$', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))

for i in range(0, nr_letters):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

for i in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)

for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

random.shuffle(password_list)
for char in password_list:
    password += char
print(f'Your password is {password}')

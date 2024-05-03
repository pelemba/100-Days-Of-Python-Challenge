def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("Prime")
    else:
        print("Not prime")


n = int(input("Enter number you want to check: "))
prime_checker(n)

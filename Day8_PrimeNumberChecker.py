def prime_checker(number):
    bFlag=False
    for n in range(2,number-1):
        if number%n==0:
            bFlag=True
    if (bFlag):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

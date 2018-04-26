
# Check two strings are anagram 
# Check tow strings are palindrome 
# Check if number is prime 
# print factorial of number
# String permuation

def is_prime(n):
    x = True
    for i in range(2, n):
        if n%i == 0:
            x = False
            break
    return x

def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n = n-1
    print fact


def isPowerOFF(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            return False
    return True

test = "sakthi dasan sekar"
print list(test)
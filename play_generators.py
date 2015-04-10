# Let's play with Python generators!
# Sources:
# 1. http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
import math

def get_primes(input_list):
    return [
        element for element
        in input_list
        if is_prime(element)
    ]


def is_prime(number):
    if number > 1:  # Only check numbers greater than 1
        if number == 2:  # 2 is a prime number
            return True
        if number % 2 == 0:  # It is not prime if it is divisible by 2
            return False
        for num in range(3, int(math.sqrt(number) + 1), 2):
            if number % num == 0:
                return False
        return True
    return False


# Generator implementation
def get_primes_2(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


# Project Euler #10

def get_primes_under_two_million():
    # Sum of all the primes below two million
    total = 2

    for next_prime in get_primes_2(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print total
            return


get_primes_under_two_million()

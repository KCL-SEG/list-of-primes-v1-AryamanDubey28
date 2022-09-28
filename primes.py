"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    counter = 2
    while len(list) != number_of_primes:
        if isPrimeChecker(counter):
            list.append(counter)
        counter+=1
    return list


def isPrimeChecker(number):
    for i in range(1,number):
        if number % i == 0 and i != 1:
            return False   
    return True





# Write a script which displays the sum of the first 100 prime numbers
import math

def isPrime(number : int) -> bool:
    if (number == 0) or (number == 1):
        return False
    if (number == 2):
        return True
    for i in range(2, (math.ceil(math.sqrt(number)))):
        if number % i == 0:
            return False
    return True

def first_n_prime_numbers(n : int) -> tuple:
    result_list = []
    counter = 0
    test_number = 0
    sum = 0
    while counter < n :
        if isPrime(test_number):
            result_list.append(test_number)
            counter += 1
            sum += test_number
        test_number += 1
    return sum, result_list

if __name__ == "__main__":
    n = 10
    print(first_n_prime_numbers(n))
    m = 100
    print(first_n_prime_numbers(m))
    
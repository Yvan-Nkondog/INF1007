# Find all the prime numbers within a given range.
import math

# Function to identify individual prime numbers
def is_prime(number : int) -> bool:
    if ((number == 0) or (number == 1)):
        return False
    if (number == 2):
        return True
    for i in range(2, math.ceil(math.sqrt(number) ) + 1):
        if ((number % i) == 0):
            return False
    return True

# Function to extract he prime numbers in a range
def prime_numbers_in_range_mn(m: int, n: int) -> list:
    result = []
    for i in range(m, n+1):
        if is_prime(i):
            result.append(i)
    return result


if __name__ == "__main__":
    for j in range(10):
        print(j, is_prime(j))
    
    lower_bound = 10
    upper_bound = 30
    print(prime_numbers_in_range_mn(lower_bound, upper_bound))


    
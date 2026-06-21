
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
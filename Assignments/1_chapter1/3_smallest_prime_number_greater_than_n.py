
# Find the smallest prime number greater than an interger n

from is_prime_number import is_prime


def smallest_prime_number_greater_than_n(n : int) -> int:
    counter = n + 1
    while True:
        if is_prime(counter):
            return counter
        counter += 1


if __name__ == "__main__":
    for i in range(20):
        print(i, smallest_prime_number_greater_than_n(i))

    print(smallest_prime_number_greater_than_n(10000))












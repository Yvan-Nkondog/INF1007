
# Write a python script that computes the factorial of a number.

def factorial(number : int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


if __name__ == "__main__":
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    for j in range(len(numbers)):
        print(numbers[j], factorial(numbers[j]))
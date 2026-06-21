
# Function to determine the maximum value between three numbers
# without using special function

def max_value(a: float, b: float, c: float) -> float:
    max_val = a
    if (max_val < b):
        max_val = b
    if (max_val < c):
        max_val = c
    return max_val


if __name__ == "__main__":
    print(max_value(5, -2, 7))
    print(max_value(-2, -7, -9.5))
    
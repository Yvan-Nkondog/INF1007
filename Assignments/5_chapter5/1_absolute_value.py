
# Write a script that prints a number and displays its absolute value
# a) without using special functions
# b) using special functions

def compute_absolute_value(x : float) -> float:
    if x < 0:
        return -x
    return x

def compute_absolute_value_2(x: float) -> float:
    return abs(x)


if __name__ == "__main__":
    x1 = -3.5
    x2 = 5.5
    x3 = 10.3
    x4 = -0.005
    print(compute_absolute_value(x1))
    print(compute_absolute_value(x2))
    print(compute_absolute_value(x3))
    print(compute_absolute_value(x4))
    print(compute_absolute_value_2(x1))
    print(compute_absolute_value_2(x2))
    print(compute_absolute_value_2(x3))
    print(compute_absolute_value_2(x4))

# Write a program that computes the mean of 3 numbers
def compute_mean(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3

if __name__ == "__main__":
    print(compute_mean(1, 3, 5))
    print(compute_mean(1, -4, -3))
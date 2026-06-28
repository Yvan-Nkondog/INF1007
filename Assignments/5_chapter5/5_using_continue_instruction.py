
# Use the continue instruction to print all the numbers between 1 and 10, except 5

if __name__ == "__main__":
    for i in range(1, 10):
        if i == 5:
            continue
        print(i)

# Write a script which multiplies each entry of a
# a list of integers

def multiply_list_entries(user_list: list[int], value: int) -> list[int]:
    return [(element * value) for element in user_list]


if __name__ == "__main__":
    multiplication_value = 5
    list1 = [1, 2, 4, 5, 10]
    print(multiply_list_entries(list1, multiplication_value))
            
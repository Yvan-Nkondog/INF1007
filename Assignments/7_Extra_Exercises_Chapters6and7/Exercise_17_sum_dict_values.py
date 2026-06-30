
# Write a script which sums all the values inside a dictionary
def sum_dict_values(user_dict: dict) -> float:
    return sum(user_dict.values())


if __name__ == "__main__":
    user_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(sum_dict_values(user_dict))
    
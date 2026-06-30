
# Write a Python script that removes the spaces
# found between dict key names.
# Data : {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
# Expected output : {'S001': ['Math', 'Science'], 'S002': ['Math', 'Anglais']}

def remove_spaces_in_dict_key_names(user_dict: dict) -> dict:
    result_dict = {}
    for key, value in user_dict.items():
        new_key = key.replace(' ', '')
        result_dict[new_key] = value
    return result_dict


if __name__ == "__main__":
    user_dict = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
    print(remove_spaces_in_dict_key_names(user_dict))

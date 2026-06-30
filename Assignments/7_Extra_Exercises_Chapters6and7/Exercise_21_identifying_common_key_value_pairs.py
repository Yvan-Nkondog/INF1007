
# Write a script that identifies the common key-value pairs in two
# distinct dictionaries.

def get_common_key_value_pairs(user_dict1: dict, user_dict2: dict) -> dict:
    return {key: value for key, value in user_dict1.items() if (key in user_dict2) and (user_dict2[key] == value)}

if __name__ == "__main__":
    first_dict = {'key1': 1, 'key2': 3, 'key3': 2}
    second_dict = {'key1': 1, 'key2': 2}
    third_dict = {'key1': 1, 'key2': 0, 'key3': 2}
    print(get_common_key_value_pairs(first_dict, second_dict))
    print(get_common_key_value_pairs(first_dict, first_dict))
    print(get_common_key_value_pairs(first_dict, third_dict))

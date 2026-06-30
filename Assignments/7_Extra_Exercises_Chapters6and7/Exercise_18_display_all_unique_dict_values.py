
# Write a script that displays all the unique values of a dictionary.
# For example : Data :: {"I":"S001", "II": "S002", "III": "S001", "IV": "S005", "V":"S005", 
# "VI":"S009","VII":"S007"}
# Expected output : {'S002', 'S005', 'S007', 'S009', 'S001'}

def set_of_dict_values(user_dict: dict) -> set:
    return set(user_dict.values())

# Exercise : Transforme the structure as shown below : 
# Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
#{"V":"S009"},{"VIII":"S007"}]
# Expected output : {'S005', 'S002', 'S007', 'S001', 'S009'}

def get_unique_dictionary_values_from_list_of_dict(user_dict_list: list[dict]) -> set:
    return set([(user_dict_list[index]).values() for index, element in enumerate(user_dict_list)])


if __name__ == "__main__":
    user_dict = {"I":"S001", "II": "S002", "III": "S001", "IV": "S005", "V":"S005", "VI":"S009","VII":"S007"}
    print(set_of_dict_values(user_dict))
    user_dict_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
                    {"V":"S009"},{"VIII":"S007"}]
    get_unique_dictionary_values_from_list_of_dict(user_dict_list)

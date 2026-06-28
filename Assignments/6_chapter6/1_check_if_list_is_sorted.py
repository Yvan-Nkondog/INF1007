
# Write a program which asks a user to input 10 values (int, float, str),
# then checks if these values are sorted.


def input_value() -> list:
    phrase = input("Please enter 10 values (string, int or float), separated by a space : ")
    return phrase
    

def sort_list(list_user: list) -> bool:
    values = list_user.split()
    floating_point_values = [float(value) for value in values]
    sorted_values = sorted(floating_point_values)
    print(floating_point_values)
    print(sorted_values)
    return sorted_values == floating_point_values


if __name__ == "__main__":
    value_list = input_value()
    print(sort_list(value_list))


# Write a script which moves each element in a list by one position.
# [0, 1, 2, 3, 4, 5] becomes [5, 0, 1, 2, 3, 4]

def move_by_one_position(user_list: list) -> list:
    result_list = []
    result_list.append(user_list[-1])
    for i in range(len(user_list) - 1):
        result_list.append(user_list[i])
    return result_list


# Write a script which move each element in a list by one position.
# [0, 1, 2, 3, 4, 5] becomes [1, 0, 3, 2, 5, 4]
def swap_elements_pair_wise(user_list: list) -> list:
    result_list = []
    for i in range(len(user_list)):
        if i % 2 == 0:
            result_list.append(user_list[i+1])
        else:
            result_list.append(user_list[i-1])
    return result_list


def swap_elements_pair_wise_list_comprehension_version(user_list: list) -> list:
    return [user_list[i+1] if i % 2 == 0 else user_list[i-1] for i in range(len(user_list))]


if __name__ == "__main__":
    list1 = [0, 1, 2, 3, 4, 5]
    print(move_by_one_position(list1))
    print(swap_elements_pair_wise(list1))
    print(swap_elements_pair_wise_list_comprehension_version(list1))

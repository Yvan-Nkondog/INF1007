
# Write a script that replaces the last element of a
# list with a new list
import copy

def replace_last_list_element_with_new_list(user_list: list, new_list: list) -> list:
    result_list = [element for index, element in enumerate(user_list) if (index != (len(user_list) -1))]
    result_list.extend(new_list)
    return copy.deepcopy(result_list) # deepcopy used to cut the link between the sublists.

def replace_last_list_element_with_new_list_using_slice(user_list: list, new_list: list) -> list:
    return copy.deepcopy(user_list[:-1] + new_list) # deepcopy used to cut the link between the sublists.


if __name__ == "__main__":
    list1 = [1, 2, 3, [4], 5, [6]]
    list2 = [1, [2], 3, 4]
    list3 = replace_last_list_element_with_new_list(list1, list2)
    list4 = replace_last_list_element_with_new_list_using_slice(list1, list2)
    print(list3)
    print(list4)
    list1[3][0] = 1000
    print(list1)
    print(list3)
    print(list4)

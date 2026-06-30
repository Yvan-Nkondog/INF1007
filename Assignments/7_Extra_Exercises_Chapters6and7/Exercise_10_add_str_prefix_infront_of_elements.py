
# Write a script that adds a string prefix infront of each
# list element

def add_prefix_infron_of_each_element(user_list: list, prefix: str) -> list:
    return [(prefix + str(element)) for element in user_list]


if __name__ == "__main__":
    list1 = [1, 3, 7, 15]
    list2 = [0.38, 0.11, 0.21]
    list3 = ['a', 'b', 'c', 'd']
    prefix = "ABC"
    print(add_prefix_infron_of_each_element(list1, prefix))
    print(add_prefix_infron_of_each_element(list2, prefix))
    print(add_prefix_infron_of_each_element(list3, prefix))

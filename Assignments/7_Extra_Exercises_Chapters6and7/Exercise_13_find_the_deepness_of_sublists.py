
# Write a script that determines the level of
# the deepest sublist in a list.
# For example : [[1, [[2, 3, [2]]]], [], [3]] returns 5

def get_deepest_sublist_level(user_list: list) -> int:
    corresponding_string = str(user_list)
    counter = 0
    counter_list = []
    for element in corresponding_string:
        if element == '[':
            counter += 1
            counter_list.append(counter)
        elif element == ']':
            counter -= 1
    return max(counter_list)


if __name__ == "__main__":
    list1 = [[1, [[2, 3, [2]]]], [], [3]]
    list2 = []
    list3 = [1]
    list4 = [[]]
    list5 = [[], [], []]
    print(get_deepest_sublist_level(list1))
    print(get_deepest_sublist_level(list2))
    print(get_deepest_sublist_level(list3))
    print(get_deepest_sublist_level(list4))
    print(get_deepest_sublist_level(list5))

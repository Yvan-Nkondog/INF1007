
# Write a script that extends a list without using append
# and extend functions.

def extend_list(user_list1: list, user_list2: list) -> list:
    return user_list1[:] + user_list2[:]

def extend_list_version2(user_list1: list, user_list2: list) -> list:
    return user_list1 + user_list2

# Test function to compare the results (mainly for lists of lists)
def extend_list_using_extend(user_list1: list, user_list2: list) -> list:
    user_list1.extend(user_list2)
    return user_list1

if __name__ == "__main__":
    list1 = [1, 2, 3, [4], 5, [6]]
    list1_bis = [1, 2, 3, [4], 5, [6]]
    list2 = [1, [2], 3, 4]
    empty_list = []
    list3 = extend_list(list1, list2)
    list4 = extend_list_version2(list1, list2)
    list5 = extend_list_using_extend(list1_bis, list2)
    list6 = extend_list(empty_list, list2)
    list7 = extend_list(list2, empty_list)
    print(list1)
    print(list3)
    print(list4)
    print(list5)
    list1[3][0] = 1000
    list1_bis[3][0] = 1000
    print(list3)
    print(list4)
    print(list5)

    print(list6)
    print(list7)

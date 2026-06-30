
# Write a script which checks if a list contains a sub-list.
# e.g [1, 2, 3, 4, 5, 6] contient [3, 4, 5]
# Note : The order of elements is important.

def contains_sub_list(main_list: list, sub_list: list) -> bool: 
    # Convert to str, remove external parentheses, then compare.
    return ((str(sub_list))[1:-1]) in str(main_list)


if __name__ == "__main__":
    main_list1 = [1, 2, 3, 4, 5, 6]
    sub_list1 = [3, 4, 5]
    main_list2 = [2 , 4 , 3 , 5 , 7]
    sub_list2 = [4, 3]
    sub_list3 = [3, 7]
    print(contains_sub_list(main_list1, sub_list1))
    print(contains_sub_list(main_list2, sub_list2))
    print(contains_sub_list(main_list2, sub_list3))

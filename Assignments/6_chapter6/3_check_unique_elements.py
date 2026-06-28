
# Write a script which checks if a list contains each element only once.

def is_distinct_element_list(my_list: list) -> bool:
    return len(my_list) == len(set(my_list))


if __name__ == "__main__":
    list1 = [1, 'abc', 3, 5, 7]
    list2 = [1, 'abc', 3, 5, 7, 1]
    print(is_distinct_element_list(list1))
    print(is_distinct_element_list(list2))
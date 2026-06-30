
# Remove elements appearing in a list more than once
# without using set or special functions.
# Example : [1,2,3,3,3,3,4,5] devient [1, 2, 3, 4, 5]

def remove_multiple_elements(user_list: list) -> list:
    set_list = []
    for element in user_list:
        if element not in set_list:
            set_list.append(element)
    return set_list

if __name__ == "__main__":
    list1 = [1,2,3,3,3,3,4,5]
    print(remove_multiple_elements(list1))

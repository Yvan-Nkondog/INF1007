
# Write a scipt that checks if a list is empty.

def is_empty(user_list: list) -> list:
    return len(user_list) == 0


if __name__ == "__main__":
    list1 = []
    list2 = [1]
    print(is_empty(list1))
    print(is_empty(list2))

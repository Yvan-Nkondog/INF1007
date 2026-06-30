
# Write a Python script which takes a list and returns
# the elements with odd index in another list.
# Example : [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’] becomes ['a', 'c', 'e', 'g']

def remove_even_index_elements(user_list: list) -> list:
    return [element for index, element in enumerate(user_list) if (index % 2) == 0]

if __name__ == "__main__":
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(remove_even_index_elements(list1))
    
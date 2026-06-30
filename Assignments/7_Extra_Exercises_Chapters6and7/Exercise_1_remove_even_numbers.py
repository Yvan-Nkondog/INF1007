
# Write a python script that displays the
# numbers in a list after removing all the even numbers

# Removing elements in list, which is less efficient
# has been excluded during algorithm analysis
def remove_even_numbers(elements: list) -> list:
    result_list = []
    for element in elements:
        if element % 2 != 0:
            result_list.append(element)
    return result_list

# Using list comprehension

def remove_even_numbers_list_comprehension(elements: list) -> list:
    return [element for element in elements if element % 2 != 0]


if __name__ == "__main__":
    list1 = [1.2, 5, 10.2, 10, 11, 12, 12.0, 1001, 1000]
    list2 = [-2, -3, -7, 0, 5, 2, 2.5, 3.5]
    list3 = []

    print(f"Non-even-element from {list1} without using list comprehension yields : \
        {remove_even_numbers(list1)}")
    
    print(f"Non-even-element from {list2} without using list comprehension yields : \
        {remove_even_numbers(list2)}")
    
    print(f"Non-even-element from {list3} without using list comprehension yields : \
        {remove_even_numbers(list3)}")

    print(f"Non-even-element from {list1} using list comprehension yields : \
        {remove_even_numbers_list_comprehension(list1)}")
    
    print(f"Non-even-element from {list2} using list comprehension yields : \
        {remove_even_numbers_list_comprehension(list2)}")
    
    print(f"Non-even-element from {list3} using list comprehension yields : \
        {remove_even_numbers_list_comprehension(list3)}")
    
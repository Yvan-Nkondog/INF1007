
# Write a script that returns the second largest element of
# a list.

# position = 1 for the largest element, position = 2 for the second largest element, etc.
# The following function takes into account list with elements repeating.
# Hence, the position parameters is measured with respect to the number of unique elements
# inside the list, and not to the length of the overall list (which could include duplicates).
def nth_largest_element(user_list: list, position: int) -> float:
    if position < len(set(user_list)):
        return (sorted(list(set(user_list)), reverse=True))[position - 1]
    else:
        print(f"Sorry, index {position} is out of range. ")

if __name__ == "__main__":
    list1 = [1, 2, 2, 2, 3, 4, 5, 5]
    list2 = [1, 2, 3, 4, 4, 4, 5, 5]
    list3 = [1, 10, 20, 30]
    list4 = [50, 70, 90]
    list5 = [1, 2, 2, 2, 3, 4, 5, 5, -7]
    list6 = [1, 2, 3, 4, -3, 4, 5, 5, 4]
    list7 = [10, 10, 10, 10, 10]
    list8 = [-8.3, -2.1, -12, -100.5, -2.03]
    list9 = [90]
    list10 = []

position = 2
print(f"The second largest element of the list {list1} is {nth_largest_element(list1, position)}. ")
print(f"The second largest element of the list {list2} is {nth_largest_element(list2, position)}. ")
print(f"The second largest element of the list {list3} is {nth_largest_element(list3, position)}. ")
print(f"The second largest element of the list {list4} is {nth_largest_element(list4, position)}. ")
print(f"The second largest element of the list {list5} is {nth_largest_element(list5, position)}. ")
print(f"The second largest element of the list {list6} is {nth_largest_element(list6, position)}. ")
print(f"The second largest element of the list {list7} is {nth_largest_element(list7, position)}. ")
print(f"The second largest element of the list {list8} is {nth_largest_element(list8, position)}. ")
print(f"The second largest element of the list {list9} is {nth_largest_element(list9, position)}. ")
print(f"The second largest element of the list {list10} is {nth_largest_element(list10, position)}. ")

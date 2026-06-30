
# Write a Python script that presents the difference between two lists.

# The following code permits to treat cases in which the difference between
# two lists lies only in repeated elements, with both lists of the same sizes.
# Observe the test list samples in main section for more details.

from collections import deque

# Deque (from collection) is used in this case because the implementation below 
# removes elements inside a container many times. In this case, the linked-list is better
# than the sequential list.
def lists_difference(list1: list, list2: list) -> list:
    double_ended_queue1 = deque(list1)
    double_ended_queue2 = deque(list2)
    for element in list1:
        if element in double_ended_queue2:
            double_ended_queue1.remove(element)
            double_ended_queue2.remove(element)
    
    double_ended_queue1.extend(double_ended_queue2)
    return list(double_ended_queue1)


if __name__ == "__main__":
    list1 = [1, 2, 2, 2, 3, 4, 5, 5]
    list2 = [1, 2, 3, 4, 4, 4, 5, 5]
    list3 = [1, 10, 20, 30]
    list4 = [50, 70, 90]
    list5 = [1, 2, 2, 2, 3, 4, 5, 5, -7]
    list6 = [1, 2, 3, 4, -3, 4, 5, 5, 4]
    list7 = []

    print(f"The difference between {list1} and {list1} is {lists_difference(list1, list1)}")
    print(f"The difference between {list1} and {list2} is {lists_difference(list1, list2)}")
    print(f"The difference between {list1} and {list3} is {lists_difference(list1, list3)}")
    print(f"The difference between {list1} and {list4} is {lists_difference(list1, list4)}")
    print(f"The difference between {list5} and {list6} is {lists_difference(list5, list6)}")
    print(f"The difference between {list1} and {list7} is {lists_difference(list1, list7)}")
    print(f"The difference between {list7} and {list7} is {lists_difference(list7, list7)}")

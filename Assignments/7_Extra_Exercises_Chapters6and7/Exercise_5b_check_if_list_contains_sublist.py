
# Write a script which checks if a list contains a sub-list.
# e.g [1, 2, 3, 4, 5, 6] contient [3, 4, 5]
# Note : The order of elements is important.

# This exercise repeats exercise 5, but takes
# into account subsets of lists that are non 
# consecutif. 
# This code is used to compare sublists when
# there are repeating elements, hence the simple
# set(list) cannot be used to replace this function.
# Example : [1, 3, 2, 2, 5, 4, 5] is a subset of [1, 2, 2, 2, 3, 4, 5, 5]
# with duplicates conserved.

from collections import deque

def contains_sublist_non_consecutive(user_list: list, sublist: list) -> bool:
    user_deque = deque(user_list)
    sub_deque = deque(sublist)
    for element in sublist:
        if element in user_deque:
            user_deque.remove(element)
            sub_deque.remove(element)
    # If the sub-deque is empty at the end, then the sublist is a subset of the main list
    return len(sub_deque) == 0


if __name__ == "__main__":
   
    main_list1 = [1, 2, 3, 4, 5, 6]
    sub_list1 = [3, 4, 5]
    main_list2 = [2 , 4 , 3 , 5 , 7]
    sub_list2 = [4, 3]
    sub_list2_bis = [7, 3]
    main_list3 = [1, 2, 2, 2, 3, 4, 5, 5]
    main_list3_bis = [1, 2, 3, 4, 4, 4, 5, 5]
    sub_list3 = [1, 3, 2, 2, 5, 4, 5]
    sub_list_empty = []

    print(contains_sublist_non_consecutive(main_list1, sub_list1))
    print(contains_sublist_non_consecutive(main_list2, sub_list2))
    print(contains_sublist_non_consecutive(main_list2, sub_list2_bis))
    print(contains_sublist_non_consecutive(main_list3, sub_list3))
    print(contains_sublist_non_consecutive(main_list3_bis, sub_list3)) # Element [2] expected to remain.
    print(contains_sublist_non_consecutive(sub_list3, sub_list_empty))
    

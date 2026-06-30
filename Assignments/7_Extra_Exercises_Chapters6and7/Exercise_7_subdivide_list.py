
# Write a program which divides a list into sublists of size 5.
# Example of output for a list going from 1 to 20.
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

def generate_list_of_subsets_of_size_n(user_list: list, subset_size: int) -> list:
    result_list = []
    if subset_size < len(user_list):
        subset_list = []
        for index, element in enumerate(user_list):
            subset_list.append(element)
            if (len(subset_list) == subset_size) or (index == (len(user_list) - 1)):
                result_list.append(subset_list)
                subset_list = []
    else:
        print(f"Sorry, the size of the subsets can not be greater than or equal to to the size of the main list.")
    return result_list


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    subset_size = 5
    subset_size2 = 4
    subset_size3 = 20
    subset_size4 = 19
    print(generate_list_of_subsets_of_size_n(list1, subset_size))
    print(generate_list_of_subsets_of_size_n(list1, subset_size2))
    print(generate_list_of_subsets_of_size_n(list1, subset_size3))
    print(generate_list_of_subsets_of_size_n(list1, subset_size4))
    print(generate_list_of_subsets_of_size_n(list2, subset_size))

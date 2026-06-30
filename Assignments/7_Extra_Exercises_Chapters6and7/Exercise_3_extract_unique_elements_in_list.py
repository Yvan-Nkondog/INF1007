
# write a script that extracts the unique elements in a list.

def extract_unique_elements(user_list: list) -> list:
    return list(set(user_list))

if __name__ == "__main__":
    list1 = [1, 2, 2, 2, 3, 4, 5, 5]
    list2 = [1, 2, 3, 4, 4, 4, 5, 5]
    list3 = [1, 10, 20, 30]
    list4 = [50, 70, 90]
    list5 = [1, 2, 2, 2, 3, 4, 5, 5, -7]
    list6 = [1, 2, 3, 4, -3, 4, 5, 5, 4]
    list7 = []

    print(f"The list {list1} without any element appearing twice is : {extract_unique_elements(list1)}.")
    
    print(f"The list {list2} without any element appearing twice is : {extract_unique_elements(list2)}.")
    
    print(f"The list {list3} without any element appearing twice is : {extract_unique_elements(list3)}.")
    
    print(f"The list {list4} without any element appearing twice is : {extract_unique_elements(list4)}.")
    
    print(f"The list {list5} without any element appearing twice is : {extract_unique_elements(list5)}.")
    
    print(f"The list {list6} without any element appearing twice is : {extract_unique_elements(list6)}.")

    print(f"The list {list7} without any element appearing twice is : {extract_unique_elements(list7)}.")
    
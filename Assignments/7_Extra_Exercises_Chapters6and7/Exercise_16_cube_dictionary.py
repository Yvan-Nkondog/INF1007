
# Construct a dictionary in which the keys are
# integers and the values are the cubes of these integers (1 to 15)

def cube_dictionary(user_list: list) -> dict:
    return {element: (element**3) for element in user_list}


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(cube_dictionary(list1))

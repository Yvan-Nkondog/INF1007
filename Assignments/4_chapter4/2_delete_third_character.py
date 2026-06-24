
# Write a script that deletes the third character of a
# string

# Admit only positive indices
def delete_nth_character(test_string: str, position_to_delete: int) -> str:
    if (position_to_delete <= (len(test_string) - 1)) and (position_to_delete >= 0):
        result_string = test_string[:position_to_delete] + test_string[position_to_delete + 1:]
    else:
        return(f"index out of range")
    return result_string


if __name__ == "__main__":
    test_string1 = "The children are playing outside."
    test_string2 = "Hello !"
    test_string3 = "How many days are comprised in a week ? "
    print(delete_nth_character(test_string1, len(test_string1)))
    print(delete_nth_character(test_string1, len(test_string1) - 2))
    print(delete_nth_character(test_string2, 0))
    print(delete_nth_character(test_string3, 5))
    print(delete_nth_character(test_string3, -2))
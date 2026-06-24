
# Write a script that replaces one character
# by another

def replace_character(test_string: str, old_character: str, new_character: str) -> str:
    if old_character not in test_string:
        return f"Error, the character {old_character} is not found in the original string : {test_string}."
    return test_string.replace(old_character, new_character)

if __name__ == "__main__":
    test_string1 = "Hello world !"
    test_string2 = "We are the champions !"
    test_string3 = "How to develop clean Python code."
    print(replace_character(test_string1, "H", "_"))
    print(replace_character(test_string2, "z", "_"))
    print(replace_character(test_string3, "o", "_"))
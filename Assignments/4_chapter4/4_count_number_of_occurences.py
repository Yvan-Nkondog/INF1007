
# Write a Python script that counts
# the number of characters in a string without using
# advanced functions.

def count_characters(test_string: str, character: str) -> int:
    counter = 0
    for char in test_string:
        if (char == character):
            counter += 1
    return counter 


if __name__ == "__main__":
    test_string1 = "Wild animals live in the forest."
    test_string2 = "Some wild animals live in the zoo."
    test_string3 = "What about domestic animals ?"
    print(count_characters(test_string1, "o"))
    print(count_characters(test_string2, "o"))
    print(count_characters(test_string3, "m"))
    print(count_characters(test_string1, "z"))
    
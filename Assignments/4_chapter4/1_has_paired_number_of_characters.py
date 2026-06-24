
# Write a script that identifies whether 
# the number of characters in a string is pair

def has_even_number_of_characters(test_string: str) -> bool:
    return (len(test_string) % 2) == 0

if __name__ == "__main__":
    test_string1 = "Good Bye !"
    test_string2 = "Hello"
    test_string3 = "Hi!"
    print(has_even_number_of_characters(test_string1))
    print(has_even_number_of_characters(test_string2))
    print(has_even_number_of_characters(test_string3))
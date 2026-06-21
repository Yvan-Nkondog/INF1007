# Using ASCII table, write code that converts upper case
# letters to lower case letters and vice versa.

def upper_to_lower_case(phrase: str) -> str:
    result = ''
    for letter in phrase:
        if (65 <= ord(letter) <= 90):
            result += chr(ord(letter) + 32)
        else:
            result += letter
    return result

def lower_to_upper_case(phrase: str) -> str:
    result = ''
    for letter in phrase:
        if (97 <= ord(letter) <= 122):
            result += chr(ord(letter) - 32)
        else:
            result += letter
    return result



if __name__ == "__main__":
    phrase1 = "The children are present."
    print(upper_to_lower_case(phrase1))

    phrase2 = "THE CITIZENS ARE WALKING."
    print(upper_to_lower_case(phrase2))

    phrase3 = "The workers enjoy a special holiday !"
    print(lower_to_upper_case(phrase3))

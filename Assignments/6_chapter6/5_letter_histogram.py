
# From a phrase furnished by the user, construct a letter
# histogram, then display all the letters occuring more than 5 times
# in descending order

def construct_frequency_histogram(phrase: str) -> dict:
    result_dict = {}
    for letter in phrase:
        if type(result_dict.get(letter)) == int:
            result_dict[letter] += 1
        else:
            result_dict[letter] = 1
    return result_dict


def display_letter(user_dict: dict) -> list:
    result_list = []
    for letter, frequency in user_dict.items():
        if frequency > 5:
            result_list.append((frequency, letter))
    result_list.sort(reverse=True)
    return result_list


if __name__ == "__main__":
    phrase = input("Pleae, enter the desired phrase : ")
    frequency_dict = construct_frequency_histogram(phrase)
    print(frequency_dict)
    print(display_letter(frequency_dict))

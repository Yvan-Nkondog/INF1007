
def are_anagrams(phrase1: str, phrase2: str) -> bool:
    phrase1, phrase2 = phrase1.upper(), phrase2.upper()
    if len(phrase1) != len(phrase2):
        return False
    for letter in phrase1:
        if letter not in phrase2:
            return False
    for letter in phrase2:
        if letter not in phrase1:
            return False
    return True

def are_anagrams_2(phrase1: str, phrase2: str) -> bool:
    return set(phrase1.upper()) == set(phrase2.upper())

if __name__ == "__main__":
    word1 = "aLEVINa"
    word2 = "NIVELAZ"
    word3 = "NIAVELA"
    print(are_anagrams(word1, word2))
    print(are_anagrams(word1, word3))
    print(are_anagrams(word2, word3))
    print("\n")
    print(are_anagrams_2(word1, word2))
    print(are_anagrams_2(word1, word3))
    print(are_anagrams_2(word2, word3))
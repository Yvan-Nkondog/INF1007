
# Write a script that counts the number of words in a sentence

def count_words_in_sentence(sentence: str) -> int:
    return len(sentence.split())


if __name__ == "__main__":
    sentence1 = "The children are not going to school today."
    sentence2 = "Tomorrow is a public holiday."
    sentence3 = "Hello world !"
    print(count_words_in_sentence(sentence1))
    print(count_words_in_sentence(sentence2))
    print(count_words_in_sentence(sentence3))
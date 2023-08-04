def count_words(text):
    """
    Receives a string of text and counts the number of words.
    :param text: string
    :return: int
    """
    return len(text.split())


def count_letters(text):
    """
    Receives a string of text and counts occurrence of each letter.
    :param text: string
    :return: dict
    """
    counter = {}

    for c in text:
        if c.lower().isalpha():
            if c.lower() in counter:
                counter[c.lower()] += 1
            else:
                counter[c.lower()] = 1

    return counter


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words_count = count_words(file_contents)
    letters_count = count_letters(file_contents)
    sorted_letters = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)

    print("--- Begin report for books/fankenstein.txt ---")
    print(f"{words_count} words found in the document\n")

    for k, v in sorted_letters:
        print(f"The {k} character was found {v} times")

    print("--- End report ---")
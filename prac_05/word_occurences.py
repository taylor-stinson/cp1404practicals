"""
CP1404 - Practicals
Word Occurrences
"""


def main():
    """Get string from user and create dictionary of word to word count"""
    word_count = create_sorted_dictionary()
    longest_word = determine_longest_string(word_count)
    for key, value in word_count.items():
        print(f"{key:<{longest_word}}:{value}")


def create_sorted_dictionary():
    """Get string from user and count occurrence of each word"""
    word_count = {}
    text = str(input("Text: "))
    words = text.split()
    words.sort()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


def determine_longest_string(string):
    """Determines length of the longest string in a list"""
    longest_string_length = 0
    for word in string:
        if len(word) > longest_string_length:
            longest_string_length = len(word)
    return longest_string_length


main()

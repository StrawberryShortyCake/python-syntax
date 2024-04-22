def print_words(word_list):

    altered_list = []

    for word in word_list:
        altered_list.append(word.upper())

    return altered_list


words = ["hello", "hey", "goodbye", "yo", "yes"]

print(print_words(words))
# must_start_with={"h", "y"})

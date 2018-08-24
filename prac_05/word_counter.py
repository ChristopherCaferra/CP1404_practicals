""" Program to count the words in a string and print the result. """

TEXT = "this is a collection of words of nice words this is a fun thing it is"


def main():
    text_list = TEXT.split()
    word_dict = add_items_to_new_dict(text_list)
    print("Text: ", TEXT)
    print_dict_table(word_dict)


def add_items_to_new_dict(text_list):
    # add string to dictionary as key and input count as value.
    word_dict = {}
    for word in text_list:
        word_dict[word] = text_list.count(word)
    return word_dict


def print_dict_table(word_dict):
    # print dictionary in table format
    for word, count in sorted(word_dict.items()):
        print("{:10} : {}".format(word, count))


main()

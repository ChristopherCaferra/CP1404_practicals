""" Program to count the words in a string and print the result. """

TEXT = "this is a collection of words of nice words this is a fun thing it is"


def main():
    text_list = TEXT.split()
    word_dict = add_items_to_new_dict(text_list)
    print("Text: ", TEXT, "\n")
    formatting_length = get_max_length_from_list(text_list)
    print_dict_table(word_dict, formatting_length)


def add_items_to_new_dict(text_list):
    # add string to dictionary as key and input count as value.
    word_dict = {}
    for word in text_list:
        word_dict[word] = text_list.count(word)
    return word_dict


def get_max_length_from_list(list):
    list.sort(key=len)
    max_length = len(list[-1])
    return max_length


def print_dict_table(word_dict, formatting_length):
    # print dictionary in table format
    print("{:^{}} | {}".format("Word", formatting_length, "Count"))
    print("{:{}} | {}".format(" ", formatting_length, " "))
    for word, count in sorted(word_dict.items()):
        print("{:{}} | {:>5}".format(word, formatting_length, count))


main()

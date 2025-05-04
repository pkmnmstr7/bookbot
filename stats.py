def count_the_words(book_contents):
    book_string = book_contents.split()
    return len(book_string)

def character_count(book_string):
    alpha_only = ''.join([char for char in book_string if char.isalpha()])
    listed_words = list(alpha_only.lower())
    char_dict = {

    }
    for c in listed_words:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(char_dict):
    return char_dict[1]

def dict_to_list(char_dict):
    list_of_dict = list(char_dict.items())
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
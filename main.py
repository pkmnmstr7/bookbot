import sys
from stats import count_the_words
from stats import character_count
from stats import dict_to_list

if len(sys.argv) < 2:
    print("Error: not enough arguments")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print("Usage correct")

file_path = sys.argv[1]

def get_book_text(book):
    contents = book.read()
    return contents

def main():
    with open(file_path) as f:
        book_as_string = get_book_text(f)
        book_as_string.isalpha()
        total = count_the_words(book_as_string)
        char_dictionary = character_count(book_as_string)
        sorted_counts = dict_to_list(char_dictionary)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count -----------")
        print(f"Found {total} total words")
        print("--------- Character Count ---------")
        #print(f"Character counts: {char_dictionary}")
        #print(type(sorted_counts))
        for line in sorted_counts:
            print(f"{line[0]}: {line[1]}")
        print("=============== END ===============")

main()
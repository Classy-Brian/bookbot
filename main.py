from stats import get_word_count, get_count_characters, print_report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        
        text = get_book_text(path_to_file)
        word_count = get_word_count(path_to_file)
        char_count = get_count_characters(text)

        print_report(char_count, word_count, path_to_file)


main()
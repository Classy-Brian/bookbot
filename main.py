from stats import get_word_count, get_count_characters, print_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    
    text = get_book_text(path_to_file)
    word_count = get_word_count(path_to_file)
    char_count = get_count_characters(text)

    print_report(char_count, word_count, path_to_file)


main()
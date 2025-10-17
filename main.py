from stats import get_word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    path_to_file = "books/frankenstein.txt"
    # get_book_text(path_to_file)
    get_word_count(path_to_file)

main()
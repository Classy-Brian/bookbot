def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(f" Found {word_count} total words")

def main():
    path_to_file = "books/frankenstein.txt"
    # get_book_text(path_to_file)
    get_word_count(path_to_file)

main()
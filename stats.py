def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(f" Found {word_count} total words")
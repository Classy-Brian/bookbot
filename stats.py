def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count

def get_count_characters(text):
    words = text.lower().split()
    my_dict = {}
    for word in words:
        for char in word:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict


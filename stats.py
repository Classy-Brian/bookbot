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

def sort_on(items):
    return items["num"]

def build_sorted_list(char_count):
    items = []
    for char, count in char_count.items():
        items.append({'char': char, 'num': count})
    items.sort(key=sort_on, reverse=True)
    return items

def print_report(char_count, word_count, path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    sorted_list = build_sorted_list(char_count)
    for elem in sorted_list:
        if elem['char'].isalpha():
            print(f"{elem['char']}: {elem['num']}")
    
    print("============= END ===============")
    
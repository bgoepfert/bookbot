def get_num_words(book):
    return len(book.split())

def get_num_characters(book):
    characters_dict = {}
    for char in book:
        lower_char = char.lower()
        if lower_char in characters_dict:
            characters_dict[lower_char] += 1
        else:
            characters_dict[lower_char] = 1
    
    return characters_dict

def sort_on(items):
    return items["num"]

def get_chars_as_sorted_list(dict):
    char_list = []
    for k, v in dict.items():
        char_list.append({"char": k, "num": v})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
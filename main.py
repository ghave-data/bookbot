def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_report = get_dict_report(chars_dict)
    get_report(dict_report,num_words,book_path)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    reference_char = {}
    new_text = text.lower()
    for char in new_text:
        if char in reference_char.keys():
            reference_char[char] += 1
        else:
            reference_char[char] = 1
    return reference_char

def from_dict_to_list_dict(chars_dict):
    list_dict = []
    for k,v in chars_dict.items():
        if k.isalpha():
            new_dict={}
            new_dict["char"] = k
            new_dict["num"] = v
            list_dict.append(new_dict)
        else:
            pass
    return list_dict


def get_dict_report(chars_dict):
    list_chars_dict = from_dict_to_list_dict(chars_dict)
    def sort_on(dict):
        return dict["num"]
    list_chars_dict.sort(reverse=True, key=sort_on)
    return list_chars_dict

def get_report(dict_report,num_words,path):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for d in dict_report:
        print(f"the '{d['char']}' character was found {d['num']} times")
    print("--- End report ---")


main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char = get_char(text)
    sort_on = get_sort_on(char)

    for letter in sort_on:
        if not letter["char"].isalpha():
            continue
        print(f"The '{letter['char']}' character was found {letter['num']} times")

def get_sort_on(num_char_d):
    sorted_char_dict = []
    for ch in num_char_d:
        sorted_char_dict.append({"char": ch, "num": num_char_d[ch]})
    sorted_char_dict.sort(reverse=True, key=sort_on)
    return sorted_char_dict

def sort_on(d):
    return d["num"]

def get_char(text):
    char = {}
    for c in text:
        lowered_string = c.lower()
        if lowered_string in char:
            char[lowered_string] += 1
        else:
            char[lowered_string] = 1
    return char

def get_book_text(book_path):
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

main()

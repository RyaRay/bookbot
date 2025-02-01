def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_char(text)

    character_list = []
    for char, count in character_dict.items():
        new_dict = {"name": char, "num": count}
        character_list.append(new_dict)

    character_list.sort(key=sort_on, reverse=True)

    print_report(character_list)

def get_num_words(text):
    words = text.split()
    return len(words)   


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char(text):
    new_text = text.lower()
    counts = {}
    for char in new_text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def print_report(dict):
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for d in dict:
        print(f"The '{d['name']}' character  was found {d['num']} times") 
    print("--- End Report ---")  

main()
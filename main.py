def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    characters = get_char(text)
    print(characters)


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
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts
main()
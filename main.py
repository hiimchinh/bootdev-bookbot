def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    dict = count_chars(text)
    print(dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    text_to_lower = text.lower()
    chars = {}
    for c in text_to_lower:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    return chars
main()
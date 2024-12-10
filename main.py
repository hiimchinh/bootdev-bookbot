def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    repeat_times = count_chars(text)
    sorted_dict = sort_dict(repeat_times)
    build_report(book_path, num_words, sorted_dict)

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

def sort_dict(dict):
    elements = []
    for k in dict:
        elements.append({
            'char': k,
            'num': dict[k]
        })
    def sort_on(dict):
        return dict['num']
    elements.sort(reverse=True, key=sort_on)
    result_dict = {}
    for el in elements:
        result_dict[el['char']] = el['num']
    return result_dict

def build_report(path, num_words, chars_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")

    for char in chars_dict:
        print(f"The '{char}' character was found {chars_dict[char]} times")
    print("--- End report ---")
main()
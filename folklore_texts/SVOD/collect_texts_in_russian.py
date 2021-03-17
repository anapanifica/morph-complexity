#endings of some texts in Tom 2 are deleted due to the strange regex error that I didn't manage to fix

import re

def get_book (book_title):
    path = book_title
    f = open (path, 'r', encoding = 'utf-8')
    book = f.read()
    f.close ()
    return book


def search_texts (book):
    texts = ''
    regexp = '(\n\n.*?\(.+?\)\n\n.+?(?:[\s\S](?!\n\n))+.*?\n\n)'
    res = re.findall (regexp, book)
    if res:
        for text in res:
            texts = texts + text
    return texts


def save_file (target_texts, language):
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/%s-folklore.txt' % language
    f = open (path, 'w', encoding = 'utf-8')
    f.write (target_texts)
    f.close

def main():
    texts_full = ''
    books = ["tom1.txt", "tom2.txt", "tom3.txt", "tom4.txt"]
    for book_title in books:
        book = get_book(book_title)
        texts = search_texts (book)
        texts_full = texts_full + texts
        
    save_file (texts_full, "rus")

if __name__ == '__main__':
    main()









import re

def get_book (book_title):
    path = book_title
    f = open (path, 'r', encoding = 'utf-8')
    book = f.read()
    f.close ()
    return book


def search_texts (book):
    texts = ''
    #regexp = '@([\s\S]*?)\$' #all texts in Karata
    regexp = '\$([\s\S]*?)@' #all texts in Russian
    res = re.findall (regexp, book)
    if res:
        for text in res:
            texts = texts + text
    return texts


def save_file (target_texts, language):
    #path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/%s-folk.txt' % language
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/rus_translations/%s2rus-folk.txt' % language
    f = open (path, 'w', encoding = 'utf-8')
    f.write (target_texts)
    f.close

def main():
    texts_full = ''
    book = get_book("karata-skazki.txt")
    texts = search_texts (book)
        
    save_file (texts, "kar")

if __name__ == '__main__':
    main()







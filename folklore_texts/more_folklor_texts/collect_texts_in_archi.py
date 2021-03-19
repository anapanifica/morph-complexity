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
    #regexp = '@([\s\S]*?)\$' #all texts in Archi
    regexp = '\$([\s\S]*?)@' #all texts in Russian
    res = re.findall (regexp, book)
    if res:
        for text in res:
            texts = texts + text
    return texts


def save_file (target_texts, language):
    #path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/%s-folklore.txt' % language
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/russian_translations/%s2rus-folklore.txt' % language
    f = open (path, 'w', encoding = 'utf-8')
    f.write (target_texts)
    f.close

def main():
    texts_full = ''
    book = get_book("archi_folklore.txt")
    texts = search_texts (book)
        
    save_file (texts, "arch")

if __name__ == '__main__':
    main()







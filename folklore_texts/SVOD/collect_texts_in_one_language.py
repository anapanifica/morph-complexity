#endings of some texts in Tom 2 are deleted due to the strange regex error that I didn't manage to fix

import re

def get_book (book_title):
    path = book_title
    f = open (path, 'r', encoding = 'utf-8')
    book = f.read()
    f.close ()
    return book


def search_texts (book):
    texts = []
    regexp = '(\n\n.*?\n\n.+?(?:[\s\S](?!\n\n))+.*?\n\n.*?\n)'
    res = re.findall (regexp, book)
    if res:
        for text in res:
            texts.append(text)
    return texts

def search_texts_in_a_language (texts_full, languages, language):
    target_texts = ""
    regexp2 = '\n\n([\s\S]+?)\n\n.*?\(%s\.\)\n' % languages[language]
    for text in texts_full:
        res = re.search (regexp2, text)
        if res:
            text_clean = res.group(1)
            print(text_clean)
            target_texts = target_texts + text_clean
    return target_texts


def save_file (target_texts, language):
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/folklore_texts/%s-folklore-tom4.txt' % language
    f = open (path, 'w', encoding = 'utf-8')
    f.write (target_texts)
    f.close

def main():
    texts_full = []
    #books = ["tom1.txt", "tom2.txt", "tom3.txt", "tom4.txt"]
    books = ["tom4.txt"]
    for book_title in books:
        book = get_book(book_title)
        texts = search_texts (book)
        texts_full = texts_full + texts
        
    #languages = {"rut": "рут", "ava": "авар", "agx": "агул", "dar":"дарг", "kum":"кум", "lak":"лак", "lez": "лезг",
    #             "tab":"таб", "tat":"тат", "nog":"ног", "tkr":"цах"}

    languages = {"lak":"лак"}
    for language in languages:
        print (language)
        target_texts = search_texts_in_a_language (texts_full, languages, language)
        target_texts = re.sub ("\n[0-9]+?\. ", "\n", target_texts)
        save_file (target_texts, language)

if __name__ == '__main__':
    main()







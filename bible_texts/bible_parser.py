import re

def get_txt ():
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/bible_texts/kum-x-bible.txt'
    f = open (path, 'r', encoding = 'utf-8')
    txt = f.read()
    f.close ()
    return (txt)


def txt2luke (txt):
    luke = ''
    regexp1 = '420.....\t(.*?)\n'
    res = re.findall (regexp1, txt)
    if res:
        for line in res:
            luke = luke + ' ' + line
    return luke

def save_txt (luke):
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/bible_texts/kum-luke.txt'
    f = open (path, 'a', encoding = 'utf-8')
    f.write (luke)
    f.close

def main ():
    txt = get_txt ()
    luke = txt2luke (txt)
    save_txt (luke)

if __name__ == '__main__':
    main ()

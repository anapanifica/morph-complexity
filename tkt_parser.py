import re

def get_html ():
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/tkt.html'
    f = open (path, 'r', encoding = 'utf-8')
    html = f.read()
    f.close ()
    return (html)


def html2txt (html):
    txt = ''
    regexp1 = '</button>&nbsp;&nbsp;</td><td>(.*?)</td></tr>\n<tr><td> '
    res = re.findall (regexp1, html)
    if res:
        for line in res:
            txt = txt + ' ' + line
    txt = txt.replace("    "," ")
    print (txt)
    return txt

def save_txt (txt):
    path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/tkt.txt'
    f = open (path, 'a', encoding = 'utf-8')
    f.write (txt)
    f.close

def main ():
    f1 = get_html ()
    f2 = html2txt (f1)
    f3 = save_txt (f2)

if __name__ == '__main__':
    main ()

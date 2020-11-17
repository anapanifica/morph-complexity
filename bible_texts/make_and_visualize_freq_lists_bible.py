#based on this code: https://github.com/ayushgarg31/NLP-Assignment-1

from nltk.tokenize import word_tokenize
import re
from matplotlib import pyplot as plt
from json import dumps

def tokenization (path):
    #open file and convert it to lower case
    file = open(path, "r", encoding="utf8")
    txt = file.read()
    txt_lower = txt.lower()

    #remove all special characters except - and _
    special_chars = re.compile('[`~!@#$%^&*()+={}|\[\]:";<>?,\./“”]')
    txt_lower = special_chars.sub("", txt_lower)

    #tokenize using word_tokenizer
    #token_list is a list of tokens
    tokens_list = word_tokenize(txt_lower)
    tokens_list = [i for i in tokens_list if len(re.findall('[а-яa-z0-9]', i))!=0]
    tokens = len(tokens_list)

    file.close()

    #count the number of times each token appears and save it in dictionary
    #token_count is a dictionary with tokens as keys and their frequency as value
    m = 500
    token_count = {}
    counter = 0
    unique_words = []
    for i in tokens_list:
        if (i in token_count.keys()):
            token_count[i] += 1
        else:
            token_count[i] = 1
    
        #count types after every m tokens for Heap's law
        if (counter%m == 0):
            unique_words.append(len(token_count.keys()))
        counter += 1
        
    unique_words = unique_words[1:]
    types = len(token_count.keys())
    ttr = types/tokens

    print("\nText : ", path)
    print ("The total number of tokens are : ", tokens)
    print ("Different types of tokens are : ", types)
    print ("The TTR (Type by Tokens Ratio) is :", ttr)

    return token_count, unique_words


def frequency_list (token_count, file_name):
    #convert dict to list and sort using frequency
    #token_ranks is a 2d-matrix with each row contaning 1 - token and 2 - it's count
    token_ranks = []
    for i in token_count:
        token_ranks.append([i, token_count[i]])
    
    token_ranks.sort(key = lambda x:x[1], reverse = True)


    with open(file_name, 'w') as file:
        file.writelines("%s\n" % place for place in token_ranks)

    print ("Top 20 tokens and their frequency : \n",token_ranks[:20])


def transform (freq_file, pure_file):

    with open(freq_file, 'r') as f:
            ar = [x.strip() for x in f.readlines()]
            for i in range(len(ar)):
                    ar[i] = int(ar[i].split()[-1][:-1])

    with open(pure_file, 'w') as f:
            for x in ar:
                    print(x, file=f)


def plot_freq_list ():
        with open("agx-luke_pure.txt", 'r') as f:
                ar1 = [float(x) for x in f.read().strip().split()][:100000]
                # ar1.reverse()

        with open("ava-luke_pure.txt", 'r') as f:
                ar2 = [float(x) for x in f.read().strip().split()][:100000]
                # ar2.reverse()

        with open("dar-luke_pure.txt", 'r') as f:
                ar3 = [float(x) for x in f.read().strip().split()][:100000]
                # ar3.reverse()

        with open("eng-luke_pure.txt", 'r') as f:
                ar4 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        with open("rus-luke_pure.txt", 'r') as f:
                ar5 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        with open("tab-luke_pure.txt", 'r') as f:
                ar6 = [float(x) for x in f.read().strip().split()][:100000]
                # ar4.reverse()

        #print(sum(ar1), sum(ar2), sum(ar3), sum(ar4))

        plt.plot(list(range(len(ar1))), ar1, label="agul (17 901 tokens)")
        plt.plot(list(range(len(ar2))), ar2, label="avar 2 (18 311 tokens)")
        plt.plot(list(range(len(ar3))), ar3, label="dargwa (17 211 tokens)")
        plt.plot(list(range(len(ar4))), ar4, label="eng (23 541 tokens)")
        plt.plot(list(range(len(ar5))), ar5, label="rus (18 072 tokens)")
        plt.plot(list(range(len(ar6))), ar6, label="tabasaran (17 766 tokens)")


        plt.ylabel('Frequency')
        plt.xlabel('rank')
        plt.legend()
        plt.show()

def plot_heap ():

    unique_words_tom = tokenization ("agx-luke.txt")[1]
    unique_words_avar1 = tokenization ("ava-luke.txt")[1]
    unique_words_avar2 = tokenization ("dar-luke.txt")[1]
    unique_words_tkt = tokenization ("eng-luke.txt")[1]
    unique_words_chir1 = tokenization ("rus-luke.txt")[1]
    unique_words_chir2 = tokenization ("tab-luke.txt")[1]

    m=500
    plt.plot([(i+1)*m for i in range(len(unique_words_tom))], [i for i in unique_words_tom], label="agul (17 901 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_avar1))], [i for i in unique_words_avar1], label="avar (18 311 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_avar2))], [i for i in unique_words_avar2], label="dargwa (17 211 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_tkt))], [i for i in unique_words_tkt], label="eng (23 541 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_chir1))], [i for i in unique_words_chir1], label="rus (18 072 tokens)")
    plt.plot([(i+1)*m for i in range(len(unique_words_chir2))], [i for i in unique_words_chir2], label="tabasaran (17 766 tokens)")
    plt.ylabel('Different types of tokens')
    plt.xlabel('Total no. of tokens')
    plt.legend()
    plt.show()

def main ():
    token_count = tokenization ("agx-luke.txt")[0]
    frequency_list (token_count, "agx-luke_freq.txt")
    transform ("agx-luke_freq.txt", "agx-luke_pure.txt")

    token_count = tokenization ("ava-luke.txt")[0]
    frequency_list (token_count, "ava-luke_freq.txt")
    transform ("ava-luke_freq.txt", "ava-luke_pure.txt")

    token_count = tokenization ("dar-luke.txt")[0]
    frequency_list (token_count, "dar-luke_freq.txt")  
    transform ("dar-luke_freq.txt", "dar-luke_pure.txt")
 

    token_count = tokenization ("eng-luke.txt")[0]
    frequency_list (token_count, "eng-luke_freq.txt")  
    transform ("eng-luke_freq.txt", "eng-luke_pure.txt")


    token_count = tokenization ("rus-luke.txt")[0]
    frequency_list (token_count, "rus-luke_freq.txt")  
    transform ("rus-luke_freq.txt", "rus-luke_pure.txt")
    
    token_count = tokenization ("tab-luke.txt")[0]
    frequency_list (token_count, "tab-luke_freq.txt")
    transform ("tab-luke_freq.txt", "tab-luke_pure.txt")

    plot_freq_list ()

    plot_heap ()


if __name__ == '__main__':
    main ()

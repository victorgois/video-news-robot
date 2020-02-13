import json
import csv


from bs4 import BeautifulSoup


def nlpFunction():

    import nltk
    from nltk.tokenize  import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from string import punctuation
    from nltk.probability import FreqDist
    from collections import defaultdict
    from heapq import nlargest

    with open('./data/output.json', 'r', encoding='utf-8') as f:
        output_dict = json.load(f)

    content = output_dict['articles']
    i = 0
    contentArray = []

    for each in content:    
        contentArray = output_dict['articles'][i]['content']
        #split_it = contentArray.lower().split()
        sentencas = sent_tokenize(contentArray)
        palavras = word_tokenize(contentArray.lower())
        palavras.remove("[")
        palavras.remove("]")
        palavras.remove("chars")
        #print(palavras)

        #stopwords = set(stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = [palavra for palavra in palavras if (palavra not in (stopwords.words('portuguese') + list(punctuation)))]
        frequencia = FreqDist(palavras_sem_stopwords)
        sentencas_importantes = defaultdict(int)
        for j, sentenca in enumerate(sentencas):
            for palavra in word_tokenize(sentenca.lower()):
                if palavra in frequencia:
                    sentencas_importantes[j] += frequencia[palavra]
        idx_sentencas_importantes = nlargest(1, sentencas_importantes, sentencas_importantes.get)
        for j in sorted(idx_sentencas_importantes):
            print(sentencas[j] + 'FIM DE LINHA')
        
        i+=1

nlpFunction()
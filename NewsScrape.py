import json
import csv
import re
import sys

data = {}
data['articles'] = []


with open('./data/data.json', encoding="utf8") as f:
    inputfile = json.load(f)
    articles = inputfile['articles']


def nlpFunction(data):

    import nltk
    import string
    from nltk.tokenize  import word_tokenize, sent_tokenize, RegexpTokenizer
    from nltk.corpus import stopwords
    from string import punctuation
    from nltk.probability import FreqDist
    from collections import defaultdict
    from heapq import nlargest

    content = ''
    
    #listPunctuation = string.punctuation
    listPunctuation = ['!','“','”','«','»','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\'',']','^','_','`','{','|','}','~']

    for each in data:
        content = each + content

    #contentArray = output_dict['articles'][each]['content']
    #split_it = contentArray.lower().split()
    sentencas = sent_tokenize(content)
    palavras = word_tokenize(content.lower())
    #palavras.remove("[")
    #palavras.remove("]")
    #palavras.remove("chars")
    #print(palavras)
    
    palavras_sem_stopwords = [palavra for palavra in palavras if (palavra not in stopwords.words('portuguese'))]
    palavras_sem_pontuacao = []
    
    for palavra in palavras_sem_stopwords:
        if (palavra not in listPunctuation and len(palavra) > 2):
            palavras_sem_pontuacao.append(palavra)
    
    frequencia = FreqDist(palavras_sem_pontuacao)
    
    sentencas_importantes = defaultdict(int)

    for j, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[j] += frequencia[palavra]
    idx_sentencas_importantes = nlargest(2, sentencas_importantes, sentencas_importantes.get)
    sentencas_final = ''
    for j in sorted(idx_sentencas_importantes):
        sentencas_final = sentencas[j] + sentencas_final
    
    #print(sentencas_final + '\n')
    
    return sentencas_final 

def keywordsFunction(data):

    import nltk
    import string
    from nltk.tokenize  import word_tokenize, sent_tokenize, RegexpTokenizer
    from nltk.corpus import stopwords
    from string import punctuation
    from nltk.probability import FreqDist
    from collections import defaultdict
    from heapq import nlargest

    content = ''
    
    #listPunctuation = string.punctuation
    listPunctuation = ['!','“','”','«','»','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\'',']','^','_','`','{','|','}','~']

    for each in data:
        content = each + content

    #contentArray = output_dict['articles'][each]['content']
    #split_it = contentArray.lower().split()
    #sentencas = sent_tokenize(content)
    palavras = word_tokenize(content.lower())
    #palavras.remove("[")
    #palavras.remove("]")
    #palavras.remove("chars")
    #print(palavras)
    
    palavras_sem_stopwords = [palavra for palavra in palavras if (palavra not in stopwords.words('portuguese'))]
    palavras_sem_pontuacao = []
    
    for palavra in palavras_sem_stopwords:
        if (palavra not in listPunctuation and len(palavra) > 2):
            palavras_sem_pontuacao.append(palavra)
    
    frequencia = FreqDist(palavras_sem_pontuacao)
    keywords = frequencia.most_common(5)
    
    return keywords 

def b9Parse(url,articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    content = []
    title = []
    div = soup.find('div', attrs = {"class":"c-single__header-content"})

    for p in soup.findAll('p'):
        content.append(p.text)

    for h in div.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)

    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def sapoParse(url,articles):   
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div1 = soup.find('div', attrs = {"class":"entry-inner"})
    content = []
    title = []

    div2 = soup.find('div', attrs = {"class":"post-inner group"})

    for p in div1.findAll('p'):
        content.append(p.text)

    for h in div2.findAll('h1'):
        title.append(h.text)
    
    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)

    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def publicoParse(url,articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story__body"})
    title = []
    div2 = soup.find('header', attrs = {"class":"story__header"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)

    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def tecnoblogParse(url, articles):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"entry"})
    title = []
    div2 = soup.find('div', attrs = {"class":"container news"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def tecmundoParse(url, articles):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"tec--article__body p402_premium"})
    title = []
    div2 = soup.find('div', attrs = {"class":"z--flex"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)

    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def papodeHomemParse(url, articles):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"small-12 large-10 large-centered columns beta-class"})
    title = []
    div2 = soup.find('header', attrs = {"class":"entry-header"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def canaltechParse(url, articles):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"content"})
    title = []
    div2 = soup.find('section', attrs = {"class":"col-xs-12 col-sm-11 col-lg-10 start-xs head-content"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def startupiParse(url, articles):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"post-content"})
    title = []
    div2 = soup.find('article', attrs = {"id":"single-post"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def meiobitParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"the_content"})
    title = []
    div2 = soup.find('div', attrs = {"class":"mobile-spacing"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def extraParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story"})
    title = []
    header = soup.find('h1', attrs = {"property": "na:headline"}).text
    title.append(header)
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    
    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def folhaParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"c-news__body"})
    title = soup.find('h1', attrs = {"class": "c-content-head__title c-content-head__title--italic"}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def uolParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"image-content-pad"})
    title = soup.find('h1', attrs = {"class": ""}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def observadorParse(url, articles):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"article-body-content obs-external-ad"})
    title = soup.find('h1', attrs = {"class": "article-head-content-headline-title"}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def bbcParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story-body__inner"})
    title = soup.find('h1', attrs = {"class": "story-body__h1"}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
        
def vejaParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    section = soup.find('section', attrs = {"class":"content"})
    title = []
    div2 = soup.find('div', attrs = {"class":"container news"})
    content = []

    for p in section.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def terraParse(url, articles):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"articleData"})
    title = []
    title = soup.find('h1').text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def jnParse(url, articles):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"t-article-content-inner js-select-and-share-1"})
    #print(div)
    title = []
    title = soup.find('h1', attrs = {'rel':'headline'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def expressoParse(url, articles):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"articleContent"})
    title = []
    title = soup.find('h1', attrs = {'class':'title'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
        
def tudocelularParse(url, articles):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.findAll('div', {"class":"textblock"})
    title = []
    title = soup.find('h1', attrs = {'class':'title'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def tsfptParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"t-abc-i-i js-article-content-rm-full js-sshow-sidebar-1-ref-content-full"})
    title = []
    title = soup.find('h1', attrs = {'class':'t-ah-title'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def olhardigitalParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"mat-txt"})
    title = []
    title = soup.find('h1', attrs = {'class':'mat-tit'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def maisfuteboliolParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"txtArtigo"})
    title = []
    title = soup.find('h1').text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def jornaldocomercioParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"noticia espacamento claro"})
    title = []
    title = soup.find('h2', attrs = {'class':'inline'}).text
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def obviousmagParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"content small-100 medium-100 large-65"})
    title = []
    div2 = soup.find('header')
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def mobileTimeParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"post-content entry-content"})
    title = []
    div2 = soup.find('div', attrs = {"class":"post-header"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })
    
def dcdmParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', {"class":"td-post-content td-pb-padding-side"})
    title = []
    div2 = soup.find('div', attrs = {"class":"td-post-header td-pb-padding-side"})
    content = []

    for p in div.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in div2.findAll('h1'):
        title.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })

def g1Parse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    paragraphs = soup.find('div', {"class":"mc-column content-text active-extra-styles "})
    titles = soup.find('div', attrs = {"class":"title"})
    subtitles = soup.find('div', {"medium-centered subtitle"})
    content = []
    subtitle = []
    title = []

    for p in paragraphs.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in titles.findAll('h1'):
        title.append(h.text)

    for h in subtitles.findAll('h2'):
        subtitle.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'subtitle': subtitle,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })    

def elpaisParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    paragraphs = soup.find('div', {"class":"a_b article_body | color_gray_dark  "})
    titles = soup.find('div', attrs = {"class":"a_hg basic | "})
    #subtitles = soup.find('div', {"medium-centered subtitle"})
    content = []
    subtitle = []
    title = []

    for p in paragraphs.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in titles.findAll('h1'):
        title.append(h.text)

    for h in titles.findAll('h2'):
        subtitle.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'subtitle': subtitle,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })    

def emParse(url, articles):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    paragraphs = soup.find('div', {"txt-serif js-article-box article-box mt-15  article-box-capitalize p402_premium"})
    titles = soup.find('div', attrs = {"col-sm-10 col-sm-offset-1 head-cover-title"})
    #subtitles = soup.find('div', {"medium-centered subtitle"})
    content = []
    subtitle = []
    title = []

    for p in paragraphs.findAll('p'):
        #print (p.text)
        content.append(p.text)
        #result.replace("\n","")
    for h in titles.findAll('h1'):
        title.append(h.text)

    for h in titles.findAll('h4'):
        subtitle.append(h.text)

    res = [sub.replace('.','. ') for sub in content]
    res = [sub.replace('«','') for sub in content]
    res = [sub.replace('»','') for sub in content]

    sentencas = nlpFunction(res)
    keywords = keywordsFunction(res)
    
    data['articles'].append({
        'title': title,
        'subtitle': subtitle,
        'content': content,
        'keywords': keywords,
        'sentencas': sentencas,
        'publishedAt': articles['publishedAt'],
        'image': articles['urlToImage'],
        'sourcename': articles['source']['name']
    })    


#SOURCE LIBRARY

#conjurData, globoData, tabData, jornaldeNegociosData, tudocelularData, infomoneyData, vejaData

#sourceLibrary = [b9Data, jnData, bbcData, uolData, dcdmData, sapoData, extraData, folhaData, terraData, tsfptData, publicoData, meiobitData, tecmundoData, expressoData, startupiData, canaltechData, tecnoblogData, observadorData, mobileTimeData, obviousmagData, papodeHomemData, olhardigitalData, maisfuteboliolData, jornaldocomercioData]

""" b9Parse('https://www.b9.com.br/120515/uber-lanca-opcao-de-viagens-de-tuk-tuk-no-brasil/')
bbcParse('https://www.bbc.com/portuguese/internacional-51311226/')
uolParse('https://noticias.uol.com.br/ultimas-noticias/reuters/2020/01/30/proposta-de-damares-de-abstinencia-sexual-de-jovens-vira-como-complementar-mas-especialistas-veem-riscos.htm')
dcdmParse('https://www.diariodocentrodomundo.com.br/trabalho-escravo-nao-e-um-desvio-mas-uma-ferramenta-do-sistema-diz-leonardo-sakamoto-por-nara-lacerda/')
sapoParse('https://pplware.sapo.pt/informacao/coronavirus-algoritmo-de-inteligencia-artificial-deu-alerta-mas/')
extraParse('https://extra.globo.com/noticias/economia/uber-lanca-opcao-tuk-tuk-em-seu-aplicativo-no-brasil-rv1-1-24221116.html')
folhaParse('https://www1.folha.uol.com.br/colunas/claudiacollucci/2020/01/fake-news-sobre-coronavirus-se-disseminam-mais-rapidamente-do-que-a-doenca.shtml')
terraParse('https://www.terra.com.br/noticias/mundo/coronavirus-e-sopa-de-morcego-teoria-de-conspiracao-e-fake-news-se-espalham-com-avanco-de-surto,29aa87ad644cb1ffdd159d2555cc4c2fd2jdhett.html')
tsfptParse('https://www.tsf.pt/portugal/politica/governo-quer-transpor-estatuto-do-denunciante-para-legislacao-nacional-este-ano--11762166.html')
publicoParse(' https://www.publico.pt/2020/01/31/mundo/noticia/redes-sociais-chinesas-fervem-criticas-directas-regime-fenomeno-raro-1902394')
meiobitParse('https://meiobit.com/416982/uber-corridas-tuk-tuk-vitoria-espirito-santo/')
tecmundoParse('https://www.tecmundo.com.br/mercado/149858-uber-aceita-boletos-transferencias-bancarias-entenda.htm')
expressoParse('https://expresso.pt/sociedade/2020-01-30-Rui-Pinto-diz-estar-em-prisao-preventiva-para-manter-escandalos-como-o-Luanda-Leaks-fechados-a-sete-chaves')
startupiParse('https://startupi.com.br/2020/01/uma-breve-historia-do-mercado-de-chatbots-no-brasil/')
canaltechParse('https://canaltech.com.br/utilitarios/google-esta-muito-perto-de-lancar-tradutor-de-idiomas-em-tempo-real-no-android-159656/')
tecnoblogParse('https://tecnoblog.net/323288/uber-cash-pre-pago-aceita-pagamento-boleto-transferencia-bancaria/')
observadorParse('https://observador.pt/opiniao/delacao-premiada/')
mobileTimeParse('https://www.mobiletime.com.br/noticias/28/01/2020/uber-oferece-viagens-de-tuk-tuk-em-vitoria-es/')
obviousmagParse('http://obviousmag.org/roberto_denser/2020/o-grande-paradoxo.html')
papodeHomemParse('https://papodehomem.com.br/afrofuturismo-or-o-que-e-porque-importa-e-quem-tem-construindo-este-movimento/')
olhardigitalParse('https://olhardigital.com.br/noticia/alphabet-tem-uma-segunda-equipe-trabalhando-com-computacao-quantica/96152')
maisfuteboliolParse('https://maisfutebol.iol.pt/pplaaf/mf-mundo/luanda-leaks-plataforma-confirma-rececao-dos-dados-de-rui-pinto')
jornaldocomercioParse('https://www.jornaldocomercio.com/_conteudo/geral/2020/01/723089-codigo-de-verificacao-de-seguranca-da-uber-estreia-em-porto-alegre.html') """


for article in articles:
    if article['source']['name'] == 'B9.com.br':
        b9Parse(article['url'], article)
    if article['source']['name'] == 'Sapo.pt':
        sapoParse(article['url'], article)
    if article['source']['name'] == 'Publico.pt':
        publicoParse(article['url'], article)
    if article['source']['name'] == 'Tecnoblog.net':
        tecnoblogParse(article['url'], article)
    if article['source']['name'] == 'Tecmundo.com.br':
        tecmundoParse(article['url'], article)
    if article['source']['name'] == 'Papodehomem.com.br':
        papodeHomemParse(article['url'], article)
    if article['source']['name'] == 'Canaltech.com.br':
        canaltechParse(article['url'], article)
    if article['source']['name'] == 'Startupi.com.br':
        startupiParse(article['url'], article)
    if article['source']['name'] == 'Meiobit.com':
        meiobitParse(article['url'], article)
    if article['url'].startswith('https://www1.folha.uol.com.br') == True:
        folhaParse(article['url'], article)
    if article['url'].startswith('https://noticias.uol.com.br') == True:
        uolParse(article['url'], article)
    if article['source']['name'] == 'Bbc.com':
        bbcParse(article['url'], article)
    #if article['source']['name'] == 'Observador.pt':
    #    observadorParse(article['url'], article)
    if article['source']['name'] == 'Terra.com.br':
        terraParse(article['url'], article)
    if article['source']['name'] == 'Expresso.pt':
        expressoParse(article['url'], article)
    if article['source']['name'] == 'Www.tsf.pt':
        tsfptParse(article['url'], article)
    if article['source']['name'] == 'Olhardigital.com.br':
        olhardigitalParse(article['url'], article)
    if article['source']['name'] == 'Maisfutebol.iol.pt':
        maisfuteboliolParse(article['url'], article)
    if article['source']['name'] == 'Jornaldocomercio.com':
        jornaldocomercioParse(article['url'], article)
    if article['source']['name'] == 'globo':


with open('./data/new-data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile)
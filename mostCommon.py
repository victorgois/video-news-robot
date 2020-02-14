import json
import csv

def b9Parse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    result = []

    for p in soup.findAll('p'):
        result.append(p.text)

    return result


def sapoParse(url):   
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"entry-inner"})
    result = []

    for p in div.findAll('p'):
        result.append(p.text)
    
    return result


def publicoParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story__body"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result
    

def tecnoblogParse(url):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"entry"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def tecmundoParse(url):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"tec--article__body p402_premium"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def papodeHomemParse(url):
    
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"small-12 large-10 large-centered columns beta-class"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def canaltechParse(url):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"content"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

""" def conjurParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {'class':'wysiwyg'}).findAll('p')

    result = []


    return div 


     for p in div.findAll('p'):
         
        result.append(p.text)   """

def startupiParse(url):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"post-content"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def meiobitParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"the_content"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def extraParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def folhaParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"c-news__body"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")

    return result

def uolParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"text"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result

def observadorParse(url):

    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"fbg-col-4 fbg-col-lg-2 center-column"})
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result

def bbcParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story-body__inner"})
    #print(div)
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result

#def tabParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    section = soup.find('section', attrs = {"section":"special-thematic special-card  um-texto claro  sem-titulo"})
    #print(div)
    result = []

    for p in section.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result

#def jornaldeNegociosParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    div = soup.find('div', attrs = {"class":"story-body__inner"})
    #print(div)
    result = []

    for p in div.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result

def vejaParse(url):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
    
    link = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    pagina = urlopen(link).read().decode('utf-8', 'ignore')
    
    soup = BeautifulSoup(pagina, "lxml")
    section = soup.find('section', attrs = {"class":"content"})
    #print(div)
    result = []

    for p in section.findAll('p'):
        #print (p.text)
        result.append(p.text)
        #result.replace("\n","")
    return result
#SOURCE LIBRARY

b9Data = b9Parse('https://www.b9.com.br/120515/uber-lanca-opcao-de-viagens-de-tuk-tuk-no-brasil/')
sapoData = sapoParse('https://pplware.sapo.pt/informacao/coronavirus-algoritmo-de-inteligencia-artificial-deu-alerta-mas/')
publicoData = publicoParse(' https://www.publico.pt/2020/01/31/mundo/noticia/redes-sociais-chinesas-fervem-criticas-directas-regime-fenomeno-raro-1902394')
tecmundoData = tecmundoParse('https://www.tecmundo.com.br/mercado/149858-uber-aceita-boletos-transferencias-bancarias-entenda.htm')
canaltechData = canaltechParse('https://canaltech.com.br/utilitarios/google-esta-muito-perto-de-lancar-tradutor-de-idiomas-em-tempo-real-no-android-159656/')
tecnoblogData = tecnoblogParse('https://tecnoblog.net/323288/uber-cash-pre-pago-aceita-pagamento-boleto-transferencia-bancaria/')
papodeHomemData = papodeHomemParse('https://papodehomem.com.br/afrofuturismo-or-o-que-e-porque-importa-e-quem-tem-construindo-este-movimento/')
#conjurData = conjurParse('https://www.conjur.com.br/2020-jan-29/opiniao-sigilo-profissional-advogado-frente-lgpd')
startupiData = startupiParse('https://startupi.com.br/2020/01/uma-breve-historia-do-mercado-de-chatbots-no-brasil/')
meiobitData = meiobitParse('https://meiobit.com/416982/uber-corridas-tuk-tuk-vitoria-espirito-santo/')
extraData = extraParse('https://extra.globo.com/noticias/economia/uber-lanca-opcao-tuk-tuk-em-seu-aplicativo-no-brasil-rv1-1-24221116.html')
#globoData = 
folhaData = folhaParse('https://www1.folha.uol.com.br/colunas/claudiacollucci/2020/01/fake-news-sobre-coronavirus-se-disseminam-mais-rapidamente-do-que-a-doenca.shtml')
uolData = uolParse('https://noticias.uol.com.br/ultimas-noticias/reuters/2020/01/30/proposta-de-damares-de-abstinencia-sexual-de-jovens-vira-como-complementar-mas-especialistas-veem-riscos.htm')
observadorData = observadorParse('https://observador.pt/opiniao/delacao-premiada/')
bbcData = bbcParse('https://www.bbc.com/portuguese/internacional-51311226/')
#tabData = tabParse('https://tab.uol.com.br/edicao/isaac-asimov/')
#jornaldeNegociosData = jornaldeNegociosParse('https://www.jornaldenegocios.pt/opiniao/detalhe/o-inicio-de-um-estado-panotico-que-tudo-ve')
vejaData = vejaParse('https://veja.abril.com.br/blog/radar/cpi-das-fake-news-ouve-envolvidos-em-disparos-de-mensagens-pro-bolsonaro/')


print(vejaData)


"""
terraData = 
jnData = 
expressoData = 
tudocelularData = 
cmjornalData = 
infomoneyData = 
agencialusaData = 
dnData = 
tsfptData = 
olhardigitalData = 
maisfuteboliolData = 
jornaldocomercioData = 
obviousmagData = 
mobileTimeData = 
dcdmData =  """

def nlpFunction(data):

    import nltk
    from nltk.tokenize  import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from string import punctuation
    from nltk.probability import FreqDist
    from collections import defaultdict
    from heapq import nlargest

    content = ''

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

    palavras_sem_stopwords = [palavra for palavra in palavras if (palavra not in (stopwords.words('portuguese') + list(punctuation)))]
    frequencia = FreqDist(palavras_sem_stopwords)
    print(frequencia.most_common(5))
    sentencas_importantes = defaultdict(int)

    for j, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[j] += frequencia[palavra]
    idx_sentencas_importantes = nlargest(3, sentencas_importantes, sentencas_importantes.get)
    for j in sorted(idx_sentencas_importantes):
        sentencas_final = ''
        sentencas_final = sentencas[j] + sentencas_final
    
    print(sentencas_final) 
    
#nlpFunction(extraData)

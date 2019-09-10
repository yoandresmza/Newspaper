import re
from collections import Counter
from newspaper import Article

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    return Counter(filter(None,re.split(r'[\W\d]+',article.text)))
    #Counter() devuelve un diccionario
    #filter(None,...) elimina de la lista las entradas vacias
    #re.split() devuelve una lista de palabras que para separarlas del todo el texto usa una regular expression como criterio
    #r'[\W\d] regular expression para separar palabras, \W caracteres que no son una palabra \d numeros y "+" es para que el criterio se aplique sobre caracteres consecutivos

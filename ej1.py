import re
from collections import Counter
from newspaper import Article

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    return Counter(re.split(r'[\W\d]+',article.text))

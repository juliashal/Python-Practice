'''Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. 
Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.'''

from bs4 import BeautifulSoup
import requests

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

#find_all('p',class_='paywall')
#p[class*="cm-in-content-"]'

with open("article.txt", "w") as f:
    for article in soup.find_all('p'):
        if article not in soup.select('p[class*="cm-in-content-"]') \
            and article not in soup.select('p[class*="BylineWrapper"]') \
                and article not in soup.select('p[class*="SiteFooter"]'):
            f.write(article.text+'\n')

with open("article.txt", "r") as f:
    print(f.read())

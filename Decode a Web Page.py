'''Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.'''

from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

for article in soup.find_all('h3'):
    print(article.text)

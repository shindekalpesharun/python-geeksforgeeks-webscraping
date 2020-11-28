import requests
from bs4 import BeautifulSoup

for pageNumber in range(1, 5):
    URL = 'https://www.geeksforgeeks.org/page/'+str(pageNumber)
    page = requests.get(URL)
    print("This is page number : " + str(pageNumber) + "\n")
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='content')
    articleList = results.find_all('article', class_='type-post')
    for article in articleList:
        print(article.find('a').string.strip())
        print(article.find('p').text.strip())
        print(article.find('a')['href'])
        print()

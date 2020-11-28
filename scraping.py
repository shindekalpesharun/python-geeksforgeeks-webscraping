import requests
from bs4 import BeautifulSoup

URL = 'https://www.geeksforgeeks.org/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='content')
job_elems = results.find_all('article', class_='type-post')
for job_elem in job_elems:
    print(job_elem.find('a').string.strip())
    print(job_elem.find('a')['href'])
    print(job_elem.find('p').text.strip())
    print()

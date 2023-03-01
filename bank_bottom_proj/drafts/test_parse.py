from bs4 import BeautifulSoup
import requests, time

links = []
for n in range(1, 5):
    html = requests.get(r'https://www.banki.ru/services/responses/list/?rate[0]=1&rate[1]=2&page=' + str(n) + '&isMobile=0').text
    soup = BeautifulSoup(html, 'html.parser')
    
    news = soup.find_all('a', class_='font-size-large')
    for x in news:  
        link = x.get('href')  
        links.append('https://www.banki.ru' + link)
    
print(links)

    # for url in links:
    #     print(url+ '\n')
    #     html = requests.get(url).text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     article = soup.find('article')
    #     print(article.find('div', class_='response-page__bank-meta').text.strip() + '\n')
    #     print(article.h1.text.strip()+ '\n')
    #     print(article.find('div', class_='article-text').text.strip()+ '\n')
    #     print('\n------------\n')
    #     time.sleep(0.3)
    
    

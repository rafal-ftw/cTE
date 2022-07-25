from bs4 import BeautifulSoup

def scrapModelsFromCurrentSite_AndSendRequestToDatabase(source):


    soup = BeautifulSoup(source, 'html.parser')
    articles = soup.find_all('article', attrs = {'data-testid' : 'listing-ad'})
    
    print("scraping started")

    for article in articles:
        link = article.find('a').get('href')
        uniqueId = link[-13:-5]
        print(link)
        print(uniqueId)

        for li in article.find('ul').find_all('li'):
            print(li.get_text())

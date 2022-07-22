from bs4 import BeautifulSoup

def scrapModelsFromCurrentSite_AndSendRequestToDatabase(source):
    soup = BeautifulSoup(source, 'html.parser')
    for article in soup.find_all('article'):
        print(article)

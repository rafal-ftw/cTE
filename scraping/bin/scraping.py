import requests
from bs4 import BeautifulSoup

def scrapModelsFromCurrentSite_AndSendRequestToDatabase(source, currentSearchParameters):


    soup = BeautifulSoup(source, 'html.parser')
    articles = soup.find_all('article', attrs = {'data-testid' : 'listing-ad'})
    
    print("scraping started")
    print(currentSearchParameters)

    for article in articles:

        requestBody = dict({
            "MANUFACTURER":"",
            "ARTICLEID":"",
            "SERIES":"",
            "GEN":"",
            "YEAR":"",
            "MILEAGE":"",
            "ENGSIZE":"",
            "FUELTYPE":"",
            "PRICE":"",
            "ARTCREATION":""
        })

        yearMileageEngineYear = []
        for li in article.find('ul').find_all('li'):
            yearMileageEngineYear.append(li.get_text())
        
        requestBody     ["YEAR"] = str(yearMileageEngineYear[0])
        requestBody     ["MILEAGE"] = yearMileageEngineYear[1]
        requestBody     ["ENGSIZE"] = yearMileageEngineYear[2]
        requestBody     ["FUELTYPE"] = yearMileageEngineYear[3]

        if len(currentSearchParameters) == 3:
            requestBody ["MANUFACTURER"] = currentSearchParameters[0].upper()
            requestBody ["SERIES"] = currentSearchParameters[1].upper()
            requestBody ["GEN"] = currentSearchParameters[2].upper()
        else:
            requestBody ["MANUFACTURER"] = currentSearchParameters[0]
            requestBody ["SERIES"]       = currentSearchParameters[1]

        uniqueId = article.find('a').get('href')[-13:-5]
        requestBody     ['ARTICLEID'] = uniqueId

        price = article.find_all('div')[3].find('span').get_text()
        requestBody     ["PRICE"]            = price

        print(requestBody)

        #TODO sendRequest()



def sendRequest(url, requestBody):
    requests.post(url, 
        json = {'body' : requestBody},
        headers = {}
        )
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. włączone filtry
# 2. komponent <main>
# 3. kazdy <article> to kolejna oferta
# 4. id inne niż 10 znakowe liczby to reklamy
# 5. cene z aut znajdziemy w 3 divie jako tekst
# 6. class contains pagination-list
# 7. <li title="Next Page">
# 7.1 - {
# "model":"x",
# "year":"z",
# "price":"y",
# "addDate":"?",
# "articleSpecificValue":""
# }

# 8. powtórz krok 2






# json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
#             '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

def scrapAllModelData(manufacturer, model):
    
    result = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
             '{"ID":20,"Name":"David Lee","Role":"Editor"}]'


    driver.get("https://www.otomoto.pl/")

    # driver.find_element(By.blablabla).send_keys(manufacturer)

    # lokalnie zapisz jsona se jako koniec funkcji
    # bo potem trzeba bedzie to wyslac do backendu za pomoca requests
    # jsona

    # kurwa


    
# {
# "search1":{
#     "manufacturer":"bmw",
#     "model":"seria 3",
#     "generation":"g30"
#     },

# "search2":{
#     "manufacturer":"bmw",
#     "model":"seria 5",
#     "generation":"f10"
#     },

# "search3":{
#     "manufacturer":"audi",
#     "model":"a4",
#     "generation":"b8"
#     }
# }



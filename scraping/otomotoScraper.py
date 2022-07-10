import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


parameter_file = open(f'{os.getcwd()}\scraping\params\parameters.json')
params = json.load(parameter_file)


def scrapAllModelData(manufacturer, model, generation):

    print(f'current manufacturer for selenium is {manufacturer}')
    print(f'current model for sele is {model}')
    print(f'current generation for selenium is {generation}')

    driver.get("https://www.otomoto.pl/")
    driver.get("https://wp.pl/")

    pass


def main():
    for key in params:
        paramsValue = params[key]
        scrapAllModelData(paramsValue["manufacturer"],
                        paramsValue["model"],
                        paramsValue["generation"])


if __name__ == "__main__":
    main()
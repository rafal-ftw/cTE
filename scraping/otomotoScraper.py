import json
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))



parameter_file = open(f'{os.getcwd()}\parameters.json')
params = json.load(parameter_file)
wait = WebDriverWait(driver, 5)

def scrapAllModelData(manufacturer, model, generation):
    print(f'current generation for selenium is {generation}')

    driver.get("https://www.otomoto.pl/")
    driver.maximize_window()

    cookiesAcceptButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookiesAcceptButton.click()

    manufacturerInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_make")))
    manufacturerInput.click()
    manufacturerInput.send_keys(manufacturer)
    manufacturerInput.send_keys(Keys.ENTER)

    modelInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_model")))
    modelInput.click()
    modelInput.send_keys(model)
    modelInput.send_keys(Keys.ENTER)

    generationInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_generation")))
    generationInput.click()
    generationInput.send_keys(generation)
    generationInput.send_keys(Keys.ENTER)

    time.sleep(2.5)

    searchButton = driver.find_element(By.CLASS_NAME, "ds-button.ds-width-full")
    searchButton.click()

    siteNextPageClick = wait.until(EC.element_to_be_clickable
                                                    ((By.XPATH, "//*[@id='__next']/div/div/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/div/ul/li[7]")))
    siteNextPageClick.click()
    


def main():
    for key in params:
        paramsValue = params[key]
        scrapAllModelData(paramsValue["manufacturer"],
                        paramsValue["model"],
                        paramsValue["generation"])
if __name__ == "__main__":
    main()
import json
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))



parameter_file = open(f'{os.getcwd()}\parameters.json')
params = json.load(parameter_file)
wait = WebDriverWait(driver, 5)

def scrapAllModelData(*args):

    searchParameters = args

    print(searchParameters)
    
    driver.get("https://www.otomoto.pl/")
    driver.maximize_window()
    

    cookiesAcceptButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookiesAcceptButton.click()

    manufacturerInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_make")))
    manufacturerInput.click()
    manufacturerInput.send_keys(searchParameters[0])
    manufacturerInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    modelInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_model")))
    modelInput.click()
    modelInput.send_keys(searchParameters[1])
    modelInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    generationInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_generation")))
    generationInput.click()
    generationInput.send_keys(searchParameters[2])
    generationInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    time.sleep(2.5)

    searchButton = driver.find_element(By.CLASS_NAME, "ds-button.ds-width-full")
    searchButton.click()

    # dodaj scroll do elementu
    siteNextPageClick = wait.until(EC.element_to_be_clickable
                                                    ((By.XPATH, "//*[@id='__next']/div/div/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/div/ul/li[7]")))
    siteNextPageClick.click()
    


def main():

    
    for searchSet in params:
        currentSearchSet = params[searchSet]
        args = []

        if "generation" not in currentSearchSet.keys():
            if "year" not in currentSearchSet.keys():
                print(f"Must provide at least generation or year of make. Current data set: {currentSearchSet}")
                break

        if "manufacturer" not in currentSearchSet:
            print(f"no manufacturer within current data set. Current data set: {searchSet}")
            break
        else:
            args.append(currentSearchSet.get("manufacturer"))

        if "model" not in currentSearchSet:
            print(f"no n wtihin current data set. Current data set: {searchSet}")
            break
        else:
            args.append(currentSearchSet.get("model"))

        if "generation" in currentSearchSet:
            args.append(currentSearchSet.get("generation"))

        if "year" in currentSearchSet:
            args.append(currentSearchSet.get("year"))

        scrapAllModelData(*args)


        


        

if __name__ == "__main__":
    main()
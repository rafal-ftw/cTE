import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bin.scraping import scrapModelsFromCurrentSite_AndSendRequestToDatabase
from bin.webdriverSettings import initiateWebDriverOptions
import bin.globals as globals

# this one is headless for testing
print(os.getcwd())
driver = webdriver.Chrome(options = initiateWebDriverOptions(), service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


def navigateThroughSpecificSetOfParameters(*args):

    wait = WebDriverWait(driver, 5)

    driver.get("https://www.otomoto.pl/")
    driver.maximize_window()

    if globals.cookieFlag == False:
        cookiesAcceptButton = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        cookiesAcceptButton.click()
        globals.cookieFlag = True
    
    if len(args) <= 3:
        try:

            #jedno podejscie, kazda akcja w linii
            manufacturerInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_make")))
            manufacturerInput.send_keys(args[0])
            driver.implicitly_wait(1)
            # checkAndCorrect(manufacturerInput, args[0])
            manufacturerInput.send_keys(Keys.RETURN)

            #drugie podejscie, action chain
            modelInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_model")))
            action.click(modelInput).send_keys(args[1]).pause(1).perform()
            # checkAndCorrect(modelInput, args[1])
            modelInput.send_keys(Keys.RETURN)

            print(len(args))

            if len(args) == 2:
                pass
            else:
                generationInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_generation")))
                action.click(generationInput).send_keys(args[2]).pause(1).perform()
                # checkAndCorrect(generationInput, args[2])
                generationInput.send_keys(Keys.RETURN)

            searchButton = driver.find_element(By.XPATH, "//button[@data-testid='submit-btn']")
            searchButton.click()

        except Exception as e:
            print(f"there has been an error! \n{e}")
        

    lastPage = False

    while lastPage != True:
        try:
            scrapModelsFromCurrentSite_AndSendRequestToDatabase(driver.page_source)

            siteNextPageButton = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@data-testid='pagination-step-forwards']")))
            action.move_to_element(siteNextPageButton).pause(2).scroll_by_amount(0, 10).click(siteNextPageButton).perform()

            
        except:
            lastPage = True
            print("You've reached last page of records, all the models are sent to the backend")
            # send post request
            break

# def checkAndCorrect(element, value):
#     if element.get_attribute != value:
#         element.clear()
#         try:
#             for i in value:
#                 element.send_keys(i)
#         except Exception as e:
#             print(f"Value provided to input is invalid, check parameters.json. \n{e}")

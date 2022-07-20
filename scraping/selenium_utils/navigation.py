import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
    
def scrapAllModelData(*args):

    wait = WebDriverWait(driver, 5)
    
    driver.get("https://www.otomoto.pl/")
    driver.maximize_window()
    
    #cookies show only one time for browser
    cookiesAcceptButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookiesAcceptButton.click()
    
    manufacturerInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_make")))
    manufacturerInput.click()
    manufacturerInput.send_keys(args[0])
    manufacturerInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    modelInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_model")))
    modelInput.click()
    modelInput.send_keys(args[1])
    modelInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    generationInput = wait.until(EC.element_to_be_clickable
                                                    ((By.ID, "filter_enum_generation")))
    generationInput.click()
    generationInput.send_keys(args[2])
    generationInput.send_keys(Keys.ENTER)
    time.sleep(0.5)

    time.sleep(2.5)

    searchButton = driver.find_element(By.CLASS_NAME, "ds-button.ds-width-full")
    searchButton.click()

    #get source
    #parse it
    #get values
    #save dictionaries in array to send to backend

    lastPage = False

    while lastPage != True:
        try:
            siteNextPageButton = wait.until(EC.element_to_be_clickable
                                                    ((By.XPATH, "//*[@data-testid='pagination-step-forwards']")))
            ActionChains(driver).move_to_element(siteNextPageButton).click(siteNextPageButton).perform()
        except:
            lastPage = True
            print("You've reached last page of records, all the models are sent to the backend")
            # send post request
            break
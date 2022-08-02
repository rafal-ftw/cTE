import time
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

driver = webdriver.Chrome(options = initiateWebDriverOptions(), service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


def navigateThroughSpecificSetOfParameters(*currentSearchParameters):
    wait = WebDriverWait(driver, 5)
    driver.get("https://www.otomoto.pl/")

    if globals.cookieFlag == False:
        cookiesAcceptButton = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        cookiesAcceptButton.click()
        globals.cookieFlag = True
    
    if len(currentSearchParameters) <= 3:
        try:

            sendKeys_Wait_PressReturn("//*[@id='filter_enum_make']", currentSearchParameters[0])

            sendKeys_Wait_PressReturn("//*[@id='filter_enum_model']", currentSearchParameters[1])

            if len(currentSearchParameters) == 2:
                pass
            else:
                sendKeys_Wait_PressReturn("//*[@id='filter_enum_generation']", currentSearchParameters[2])

            driver.implicitly_wait(1)
            searchButton = driver.find_element(By.XPATH, "//button[@data-testid='submit-btn']")
            searchButton.click()

        except Exception as e:
            print(f"there has been an error! \n{e}")
        

    lastPage = False

    while lastPage == False:

        wait.until(EC.title_contains, "osobowe - otomoto.pl")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//article[@data-testid = 'listing-ad']")))

        scrapModelsFromCurrentSite_AndSendRequestToDatabase(driver.page_source, currentSearchParameters)
        
        try:
            siteNextPageButton = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@data-testid='pagination-step-forwards']")))
            action.move_to_element(siteNextPageButton).pause(1).scroll_by_amount(0, 10).click(siteNextPageButton).perform()
        except:
            lastPage = True
            print("You've reached last page of records, all the models are sent to the backend")
            # send post request
            break

def sendKeys_Wait_PressReturn(xpath, value):
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(value)
    driver.implicitly_wait(2)
    checkAndCorrect(element, value)
    element.send_keys(Keys.RETURN)
    time.sleep(2)
    

    
def checkAndCorrect(element, value):
    if element.text != value:
        element.clear()
        try:
            for i in value:
                element.send_keys(i)
        except Exception as e:
            print(f"Value provided to input is invalid, check parameters.json. \n{e}")

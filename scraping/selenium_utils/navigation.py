import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium_utils.globals as globals

# this one is headless for testing
# driver = webdriver.Chrome(options = initiateOptions(), service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


def scrapAllModelData(*args):

    wait = WebDriverWait(driver, 5)

    driver.get("https://www.otomoto.pl/")
    driver.maximize_window()

    if globals.cookieFlag == False:
        cookiesAcceptButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookiesAcceptButton.click()
        globals.cookieFlag = True
    
    if len(args) <= 3:
        try:
            manufacturerInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_make")) )
            action.click(manufacturerInput).send_keys(args[0]).pause(1).send_keys(Keys.RETURN).perform()
            time.sleep(0.5)

            modelInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_model")))
            action.click(modelInput).send_keys(args[1]).pause(1).send_keys(Keys.ENTER).perform()
            time.sleep(0.5)

            print(len(args))

            if len(args) == 2:
                pass
            else:
                generationInput = wait.until(EC.element_to_be_clickable((By.ID, "filter_enum_generation")))
                action.click(generationInput).send_keys(args[2]).pause(0.5).send_keys(Keys.ENTER).perform()
                time.sleep(0.5)

            searchButton = driver.find_element(By.XPATH, "//button[@data-testid='submit-btn']")
            searchButton.click()

        except Exception as e:
            print(f"there has been an error! {e}")

    # get source
    # parse it
    # get values
    # save dictionaries in array to send to backend

    lastPage = False

    while lastPage != True:
        try:
            siteNextPageButton = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@data-testid='pagination-step-forwards']")))
            action.move_to_element(siteNextPageButton).pause(2).scroll_by_amount(0, 10).click(siteNextPageButton).perform()

        except:
            lastPage = True
            print("You've reached last page of records, all the models are sent to the backend")
            # send post request
            break

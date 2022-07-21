import os
from selenium import webdriver

def initiateOptions():

    adblock = f"{os.getcwd()}\scraping\selenium_utils\adblock-v1.12.4.crx"

    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_extension(adblock)
    
    return option
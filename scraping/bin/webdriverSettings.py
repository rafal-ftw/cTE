import os
from selenium import webdriver

def initiateWebDriverOptions():
    
    adblock = f"{os.getcwd()}\\bin\\adblock-v1.12.4.crx"

    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_extension(adblock)
    
    return option
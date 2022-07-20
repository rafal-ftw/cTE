from selenium import webdriver

def initiateOptions():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    
    return option
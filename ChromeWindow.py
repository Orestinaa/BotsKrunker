import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ChromeWindow:
    def __init__(self):
        # Create Chromeoptions instance
        self.options = webdriver.ChromeOptions()

        # Adding argument to disable the AutomationControlled flag
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        # Exclude the collection of enable-automation switches
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Turn-off userAutomationExtension
        self.options.add_experimental_option("useAutomationExtension", False)

        self.options.page_load_strategy = 'none'
        # Setting the driver path and requesting a page
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 20)

        # Changing the property of the navigator value for webdriver to undefined
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Initializing a list with two Useragents
        self.useragentarray = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        ]

    def getOptions(self):
        return self.options

    def getDriver(self):
        return self.driver

    def getWait(self):
        return self.wait

    def getUserAgentArray(self):
        return self.useragentarray

    def createTab(self):
        self.driver.execute_script("window.open('');")

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class KrunkerBOT:
    def __init__(self, driver, wait, URL, page):
        self.driver = driver
        self.wait = wait
        self.URL = URL
        self.page = page

    def play(self):
        # Go to the tab self.page
        print("Opening tab " + str(self.page) + "...")
        self.driver.switch_to.window(self.driver.window_handles[self.page])
        self.driver.get(self.URL)

        if self.page == 0:
            # COOKEIS
            self.wait.until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            # time.sleep(2)
            self.driver.find_element("id", "onetrust-accept-btn-handler").click()
            print("Accepted Cookies")

            # EXPERT MODE
            #time.sleep(3)
            self.wait.until(EC.presence_of_element_located((By.ID, 'expertModeBtn')))
            self.driver.find_element("id", "expertModeBtn").click()
            print("Entered Expert Mode")

            time.sleep(2)
            self.driver.get(self.URL)
            print("Joined Lobby")

        # Trova l'elemento del corpo della pagina
        self.wait.until(EC.presence_of_element_located((By.ID, 'instructions')))
        time.sleep(1)
        body_element = self.driver.find_element("tag name", "body")
        # Fai clic sul corpo della pagina
        print("Playing...")

        #if EC.visibility_of_element_located((By.ID, 'instructions')):
        #    time.sleep(2)
        #    body_element.click()
        #    print("Playing...")

    def auto_respawn(self):
        self.driver.switch_to.window(self.driver.window_handles[self.page])
        if EC.visibility_of_element_located((By.ID, 'instructions')):
            time.sleep(1)
            self.driver.find_element("tag name", "body").click()
            print("Playing...")
        if self.driver.find_element((By.CLASS_NAME, 'instructionsHeader')):
            print(EC.visibility_of_element_located((By.CLASS_NAME, 'instructionsHeader')))
            self.driver.get(self.URL)
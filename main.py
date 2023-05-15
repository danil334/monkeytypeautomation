## Be sure to have Selenium installed

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)

##from sys import exit

driver = webdriver.Chrome(executable_path="[put executable path]")


class outOfTurnException(Exception):
    pass


class usefulMethods:
    @staticmethod
    def get_element_and_click(by, element):
        w = driver.find_element(by, element)
        w.click()

    def send_keys(keys):
        ActionChains(driver).send_keys(keys).perform()


driver.get("https://monkeytype.com/")

WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[mode="words"]'))
)

usefulMethods.get_element_and_click(By.CSS_SELECTOR, 'div[mode="words"]')

driver.implicitly_wait(1)


while True:
    words = driver.find_element(By.ID, "words")

    active_word = words.find_element(By.CSS_SELECTOR, 'div[class="word active"]')

    letters = active_word.find_elements(By.TAG_NAME, "letter")

    l = []

    for letter in letters:
        l.append(letter.text)

    for letter in l:
        ActionChains(driver).send_keys(letter).perform()

    ActionChains(driver).send_keys(Keys.SPACE).perform()

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def testId(self):
        liga = driver.find_element(By.XPATH, "//a[contains(text(), 'Pagina 2')]")
        if liga is not None:
            liga.click()

        nombre = driver.find_element(By.XPATH, "//input[@id='Segundo']")
        if nombre is not None:
            nombre.send_keys("Juan")
        time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

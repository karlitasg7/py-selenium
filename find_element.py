import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def testId(self):
        elementById = driver.find_element(By.XPATH, "//*[@id='noImportante']")
        if elementById is not None:
            print("Encontramos el elemento usando XPATH")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

import time
import unittest

from selenium import webdriver


class ClickSelect(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        elemento = driver.find_element_by_xpath("//div[@id='center']/button")
        if elemento is not None:
            elemento.click()
        alerta = driver.switch_to.alert
        time.sleep(3)
        alerta.accept()
        # time.sleep(3)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

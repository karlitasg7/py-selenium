import time
import unittest

from selenium import webdriver


class ClickSelect(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        opcion = driver.find_element_by_xpath("//tr[@id='noImportante']/td[2]")
        if opcion is not None:
            print("Texto: " + opcion.text)

        opcion2 = driver.find_element_by_id("importante")
        if opcion2 is not None:
            valorAtributo = opcion2.get_attribute("class")
            print("Texto: " + valorAtributo)
        time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

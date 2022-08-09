import unittest

from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def testId(self):
        elementById = driver.find_element_by_xpath("//tr[@id='noImportante']")
        if elementById is not None:
            print("Encontramos el elemento con Id = noImportante")

    def testName(self):
        elementByName = driver.find_element_by_class_name("rojo")
        if elementByName is not None:
            print("Encontramos el elemento con class name = rojo")

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

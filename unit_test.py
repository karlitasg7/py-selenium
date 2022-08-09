import unittest

from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://clouditeducation.com/pruebas/")

    def testIdName(self):
        element = driver.find_element_by_name("ultimo")

        if element is not None:
            print("Elemento encontrado por name")

    def testId(self):
        element = driver.find_element_by_id("noImportante")

        if element is not None:
            print("Elemento encontrado por ID")

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main

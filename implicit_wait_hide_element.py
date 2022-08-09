import time
import unittest

from selenium import webdriver


class Espera(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)

        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        boton = driver.find_element_by_id("proceed")
        if boton is not None:
            boton.click()

        time.sleep(3)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

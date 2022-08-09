import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from py-selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class Espera(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        # driver.implicitly_wait(15)

        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        espera = WebDriverWait(driver, 10)
        boton = espera.until(EC.element_to_be_clickable((By.ID, "proceed")))
        if boton is not None:
            boton.click()

        time.sleep(3)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

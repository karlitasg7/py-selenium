import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class DropdownMenu(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)

        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        botonMenu = driver.find_element_by_class_name("dropbtnx")
        if botonMenu is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(botonMenu).perform()

            liga = driver.find_element_by_link_text("Link 1")
            if liga is not None:
                acciones.move_to_element(liga)
                acciones.click()
                acciones.perform()

        time.sleep(3)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

# una espera implicita es cuando el web driver espera por un tempo maximo determinado para encontrar un elemento
# solamente necesita ser llamado una sola vez por sesion
# es general, la misma espera cada vez que tratas de encontrar un elemento
# funciona durante la sesion, es decir hasta que se cierra

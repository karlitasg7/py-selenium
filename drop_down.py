import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


class ClickSelect(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        ingredients = driver.find_element_by_name("ingrediente")
        if ingredients is not None:
            ingredienteSel = Select(ingredients)
            ingredienteSel.select_by_value("cebolla")

        time.sleep(5)

    def test2(self):
        frutas = driver.find_element_by_name("Select1")
        if frutas is not None:
            frutasSel = Select(frutas)
            frutasSel.select_by_index(1)
            frutasSel.select_by_visible_text("Sandia")
        time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()

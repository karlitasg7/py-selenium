from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://clouditeducation.com/pruebas/")

    element = driver.find_element_by_name("ultimo")

    if element is not None:
        print("Elemento encontrado")

    driver.quit()

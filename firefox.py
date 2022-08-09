from selenium import webdriver


def run_firefox():
    driver = webdriver.Firefox()
    driver.get("http://www.goodstartbooks.com")

    driver.quit()


def run_chrome():
    driver = webdriver.Chrome()
    driver.get("http://www.goodstartbooks.com")

    driver.quit()


def run_ie():
    driver = webdriver.Ie()
    driver.get("http://www.goodstartbooks.com")

    driver.quit()


if __name__ == '__main__':
    run_firefox()
    run_chrome()
    run_ie()

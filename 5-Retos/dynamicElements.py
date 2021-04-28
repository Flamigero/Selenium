import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        len_menu = 5
        tries = 0
        menu = []

        while len(menu) < len_menu:
            tries += 1
            menu = driver.find_elements_by_xpath('//*[@id="content"]/div/ul/li')
            driver.refresh()

        print(f"number of tries: {tries}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
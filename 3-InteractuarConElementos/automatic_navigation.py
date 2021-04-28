import unittest
from selenium import webdriver
from time import sleep
# https://www.techbeamers.com/important-selenium-webdriver-commands/

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://google.com/')

    def test_browser_navigation(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.forward()
        sleep(2)
        self.driver.refresh()
        sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
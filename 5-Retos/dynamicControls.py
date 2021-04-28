import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        checkbox = self.driver.find_element_by_css_selector('#checkbox > input:nth-child(1)')
        checkbox.click()

        remove_add_button = self.driver.find_element_by_css_selector('#checkbox-example > button:nth-child(2)')
        remove_add_button.click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button:nth-child(1)')))
        remove_add_button.click()

        enable_disable_button = self.driver.find_element_by_css_selector('#input-example > button:nth-child(2)')
        enable_disable_button.click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button:nth-child(2)')))

        text_area = self.driver.find_element_by_css_selector('#input-example > input:nth-child(1)')
        text_area.send_keys('Platzi')
        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

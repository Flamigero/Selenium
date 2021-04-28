import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        paragraph_to_check = self.driver.find_element_by_css_selector('.example > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = self.driver.find_element_by_css_selector('.example > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            self.driver.refresh()
        
        while not found:
            if text_to_check == correct_text:
                tries += 1
                self.driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

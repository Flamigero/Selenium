import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class TestingMercadoLibre(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.get('https://www.mercadolibre.com')
        self.driver.maximize_window()

    def test_search_ps4(self):
        country = self.driver.find_element_by_id('CO')
        country.click()
        sleep(1)

        search_field = self.driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = self.driver.find_element_by_partial_link_text('Bogotá D.C.')
        self.driver.execute_script("arguments[0].scrollIntoView()", location) # Moverse hasta el elemento para que se vea en el viewport
        location.click()
        sleep(3)

        condition = self.driver.find_element_by_partial_link_text('Nuevo')
        self.driver.execute_script("arguments[0].scrollIntoView()", condition)
        condition.click()
        sleep(3)

        order_menu = self.driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price = self.driver.find_element_by_css_selector('.andes-list > li:nth-child(3) > a:nth-child(1)')
        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = self.driver.find_element_by_css_selector(f'li.ui-search-layout__item:nth-child({i+1}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h2:nth-child(1)')
            articles.append(article_name.text)

            article_price = self.driver.find_element_by_css_selector(f'li.ui-search-layout__item:nth-child({i+1}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)')
            prices.append(article_price.text)

        print(articles, prices)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
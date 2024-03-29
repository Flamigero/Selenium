import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element_by_id('select-language'))

        # Comprobar que hay 3 elementos
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        # Comprobar que las dos listas son iguales
        self.assertListEqual(exp_options, act_options)

        # Comprobar que el ingles es el idioma seleccionado
        self.assertEqual('English', select_language.first_selected_option.text)

        # Cambiar a alemán y comprobar que esté correcto
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)

        # Cambiar a inglés de nuevo
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
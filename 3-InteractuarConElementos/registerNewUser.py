import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        # Hacer click en log in
        self.driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        self.driver.find_element_by_link_text('Log In').click()
        
        # Comprobar que el botón está disponible y hacer click
        create_account_button = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        # Comprobar que el title de la página
        self.assertEqual('Create New Customer Account', self.driver.title)

        # Rellenar datos del formulario
        first_name = self.driver.find_element_by_id('firstname')
        middle_name = self.driver.find_element_by_id('middlename')
        last_name = self.driver.find_element_by_id('lastname')
        email_address = self.driver.find_element_by_id('email_address')
        news_letter_subscription = self.driver.find_element_by_id('is_subscribed')
        password = self.driver.find_element_by_id('password')
        confirm_password = self.driver.find_element_by_id('confirmation')
        submit_button = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled() and
        middle_name.is_enabled() and
        last_name.is_enabled() and
        email_address.is_enabled() and
        news_letter_subscription.is_enabled() and
        password.is_enabled() and
        confirm_password.is_enabled() and
        submit_button.is_enabled())

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
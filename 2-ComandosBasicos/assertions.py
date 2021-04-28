import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get('http://demo-store.seleniumacademy.com/')

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException:
			return False

		return True

if __name__ == '__main__':
	unittest.main(verbosity=2)
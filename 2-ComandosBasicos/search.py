import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get('http://demo-store.seleniumacademy.com/')

	def test_search_tee(self):
		search_field = self.driver.find_element_by_name('q')
		search_field.clear() # Vaciar el texto del search field

		search_field.send_keys('tee')
		search_field.submit()

	def test_search_salt_shaker(self):
		search_field = self.driver.find_element_by_name('q')

		search_field.send_keys('salt shaker')
		search_field.submit()

		products = self.driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
		self.assertEqual(1, len(products))

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)
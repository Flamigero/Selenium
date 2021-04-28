import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements to the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements")
        else:
            print("There are 0 elements")
        
        sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
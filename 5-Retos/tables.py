import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = self.driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            for j in range(4):
                row_data = self.driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
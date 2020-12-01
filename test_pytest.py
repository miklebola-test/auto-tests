from selenium import webdriver
import unittest
import pytest

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/registration2.html')


class TestBrowser(unittest.TestCase):
    def test_cite(self):
        browser.find_element_by_tag_name('div.first_block > div.form-group.first_class > input').send_keys('Mike')
        browser.find_element_by_tag_name(' div.first_block > div.form-group.second_class > input').send_keys('Lebedev')
        browser.find_element_by_css_selector(' div.first_block > div.form-group.third_class > input').send_keys('hui')
        browser.find_element_by_class_name('btn').click()
        browser.implicitly_wait(2)
        congratulations = browser.find_element_by_tag_name('h1').text
        self.assertEqual(congratulations, 'Congratulations! You have successfully registered!', 'error')

    def test_close(self):
        browser.close()


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 09/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import unittest, config
from selenium import webdriver

Init_links = config.GetSettings()
Init_connection = config.GetSettings().get_all_parameters()

#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')

#links
products                = Init_links.get_link("products")
categories              = Init_links.get_link("categories")
corporate_directory     = Init_links.get_link("corporate_directory")

#vars
Tovar_table = ".//*[@id='lists']"
category_table = ".//*[@id='is-target-4615']"
Text_filter = ".//*[@id='filters']"

class Test_Loyality_directory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(15)

    def LoginPass(self):
        driver = self.browser
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(user)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(pswd)
        driver.find_element_by_css_selector("#login > #login").click()

    def Authorize(self):
        driver = self.browser
        driver.get(srv)
        self.LoginPass()

    def test_tovar_page_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(products)
        element = driver.find_element_by_xpath(Tovar_table)
        self.assertIsNotNone(element)
        driver.close()

    def test_categories_page_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(categories)
        self.assertIsNotNone(driver.find_element_by_xpath(category_table))
        driver.close()
    def test_coprorate_directory(self):
        driver = self.browser
        self.Authorize()
        driver.get(corporate_directory)
        self.assertIsNotNone(driver.find_element_by_xpath(Text_filter))
        driver.close() 


    def tearDown(self):
        self.browser.close()
        self.browser.quit()



if __name__ == '__main__':
    unittest.main(verbosity=3)

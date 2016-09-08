#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 05/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import unittest,config
# import logging
from selenium import webdriver


#from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# logging.basicConfig(filename='unittest_log',level=logging.DEBUG)
# logging.debug('This is log message')

Init_connection = config.GetSettings().get_all_parameters()
Init_links = config.GetSettings()


#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')


#links
cards           = Init_links.get_link("cards")
members         = Init_links.get_link("members")
bonus_model     = Init_links.get_link("bonus_model")
trade_point     = Init_links.get_link("trade_point")
edit            = Init_links.get_link("edit")




# testSuite
class Test_Loyalty_Authorization_Links(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def Authorize(self):
        self.browser.get(srv)
        self.LoginPass()

    def LoginPass(self):
        username = self.browser.find_element_by_name("username")
        username.clear()
        username.send_keys(user)
        password = self.browser.find_element_by_name("password")
        password.clear()
        password.send_keys(pswd)
        password.submit()


#check log|pass
    @unittest.skip('not supported')
    def test_Authorization(self):
        self.Authorize()
        today = self.browser.find_element_by_id("for-today")
        self.assertIn('Loyality', self.browser.title)
        self.assertIsNotNone(today)
        self.browser.close()

#check link cards

    def test_link_Cards_positive(self):
        self.Authorize()
        self.browser.get(cards)
        SearchElement = self.browser.find_element_by_id('download')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link members
    # @unittest.skip('not supported')
    def test_link_members_positive(self):
        self.Authorize()
        self.browser.get(members)
        SearchElement = self.browser.find_element_by_id('block-member')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link bonus_model
    # @unittest.skip('not supported')
    def test_link_bonus_model_positive(self):
        self.Authorize()
        self.browser.get(bonus_model)
        SearchElement = self.browser.find_element_by_id('filter-status')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link trade_point
    # @unittest.skip('not supported')
    def test_link_trade_point_positive(self):
        self.Authorize()
        self.browser.get(trade_point)
        SearchElement = self.browser.find_element_by_class_name('text-info')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link edit
    # @unittest.skip('not supported')
    def test_link_edit_positive(self):
        self.Authorize()
        self.browser.get(edit)
        SearchElement = self.browser.find_element_by_id('bonus_auto')
        self.assertIsNotNone(SearchElement)
        self.browser.close()


    def tearDown(self):

        self.browser.close()
        self.browser.quit()






if __name__ == '__main__':
    unittest.main(verbosity=2)

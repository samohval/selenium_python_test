#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 07/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"


import unittest
from selenium import webdriver
import config


Init_links = config.GetSettings()
Init_connection = config.GetSettings().get_all_parameters()

#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')


#links
cards           = Init_links.get_link("cards")
card_types      = Init_links.get_link("card_types")

class Test_Loyality_cards(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def LoginPass(self):
        username = self.browser.find_element_by_name("username")
        username.clear()
        username.send_keys(user)
        password = self.browser.find_element_by_name("password")
        password.clear()
        password.send_keys(pswd)
        password.submit()

    def Authorize(self):
        self.browser.get(srv)
        self.LoginPass()


#check detailed infocard
    def test_detailed_info_card(self):
        self.Authorize()
        self.browser.get(cards)
        card_link = self.browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[3]/td[2]/a').get_attribute('href')
        self.browser.get(card_link)
        SearchElement = self.browser.find_element_by_id('kind')
        self.assertIsNotNone(SearchElement)
        self.browser.close()
        
    def test_link_card_types(self):
        self.Authorize()
        self.browser.get(card_types)
        SearchElement = self.browser.find_element_by_link_text('VIP')
        self.assertIsNotNone(SearchElement)
        self.browser.close()


    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
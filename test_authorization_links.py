#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 05/09/2016


import unittest
import logging
import ConfigParser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

_CONF_FILE = "/home/samohval/Dropbox/loyality_unit/UnitTest/test.cfg"
conf = ConfigParser.RawConfigParser()
conf.read(_CONF_FILE)
logging.basicConfig(filename='unittest_log',level=logging.DEBUG)
logging.debug('This is log message')

#authorization
srv = conf.get("connection","srv")
user = conf.get("connection","user")
pswd = conf.get("connection","pass")


#links
cards           = srv + conf.get("links","cards")
members         = srv + conf.get("links","members")
bonus_model     = srv + conf.get("links","bonus_model")
trade_point     = srv + conf.get("links","trade_point")
edit            = srv + conf.get("links","edit")
card_types      = srv + conf.get("links","card_types")



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
    def test_link_Cards(self):
        self.Authorize()
        self.browser.get(cards)
        SearchElement = self.browser.find_element_by_id('download')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link members
    def test_link_members(self):
        self.Authorize()
        self.browser.get(members)
        SearchElement = self.browser.find_element_by_id('block-member')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link bonus_model
    def test_link_bonus_model(self):
        self.Authorize()
        self.browser.get(bonus_model)
        SearchElement = self.browser.find_element_by_id('filter-status')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link trade_point
    def test_link_trade_point(self):
        self.Authorize()
        self.browser.get(trade_point)
        SearchElement = self.browser.find_element_by_class_name('text-info')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link edit
    def test_link_edit(self):
        self.Authorize()
        self.browser.get(edit)
        SearchElement = self.browser.find_element_by_id('bonus_auto')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check detailed infocard
    def test_detailed_info_card(self):
        self.Authorize()
        self.browser.get(cards)
        card_link = self.browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[3]/td[2]/a').get_attribute('href')
        self.browser.get(card_link)
        SearchElement = self.browser.find_element_by_id('kind')
        self.assertIsNotNone(SearchElement)
        self.browser.close()


    def tearDown(self):

        self.browser.close()
        self.browser.quit()






if __name__ == '__main__':
    unittest.main(verbosity=2)

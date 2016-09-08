#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 07/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"


import unittest,config,datetime
from selenium import webdriver


Init_links = config.GetSettings()
Init_connection = config.GetSettings().get_all_parameters()

#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')

#vars
today = str(datetime.datetime.now())
name_of_card_type = 'test_card_type_at '+today

#links
cards           = Init_links.get_link("cards")
card_types      = Init_links.get_link("card_types")
card_type_7     = card_types + Init_links.get_end_of_link("card_type")
card_type_edit  = card_types + Init_links.get_end_of_link("card_type_edit")


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

    # @unittest.skip('not supported')
    def test_detailed_info_card_positive(self):
        self.Authorize()
        self.browser.get(cards)
        card_link = self.browser.find_element_by_xpath('//tr[1]/td[2]/a').get_attribute('href')
        self.browser.get(card_link)
        SearchElement = self.browser.find_element_by_id('kind')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

    # @unittest.skip('not supported')
    def test_link_card_types_positive(self):
        self.Authorize()
        self.browser.get(card_types)
        SearchElement = self.browser.find_element_by_link_text('VIP')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

    # @unittest.skip('test skipped')
    def test_detailed_card_type_positive(self):
        self.Authorize()
        self.browser.get(card_type_7)
        SearchElement = self.browser.find_element_by_id('max_day_bonus')
        self.assertIsNotNone(SearchElement)
        self.assertEqual(SearchElement.get_attribute('value'),'60.000')
        self.browser.close()

    # @unittest.skip('not supported')
    def test_add_new_card_type_positive(self):
        self.Authorize()
        self.browser.get(card_type_edit)
        elem = self.browser.find_element_by_id('name')
        elem.clear()
        elem.send_keys(name_of_card_type)
        elem = self.browser.find_element_by_id('max_day_bonus')
        elem.clear()
        elem.send_keys('60.000')
        elem = self.browser.find_element_by_id('save')
        elem.click()
        #первая колонка в таблице
        elem = self.browser.find_element_by_xpath('//th[1]')
        #
        elem.click()
        elem.click()
        #
        elem = self.browser.find_element_by_link_text(name_of_card_type)
        self.assertIsNotNone(elem)
        self.browser.close()


    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=5)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 08/09/2016

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
bonus_model = Init_links.get_link("bonus_model")
coupons     = Init_links.get_link("coupons")


class Test_Loyality_bonus_models(unittest.TestCase):

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

        # @unittest.skip('not supported')
        def test_coupons_positive(self):
            self.Authorize()
            self.browser.get(coupons)
            SearchElement = self.browser.find_element_by_id('lists')
            self.assertIsNotNone(SearchElement)
            self.browser.close()
            
        # @unittest.skip('not supported')
        def test_open_model_positive(self):
            self.Authorize()
            self.browser.get(bonus_model)
            model_link = self.browser.find_element_by_xpath('//tr[1]/td[1]/a').get_attribute('href')
            self.browser.get(model_link)
            Element = self.browser.find_element_by_id('remove_restriction')
            self.assertIsNotNone(Element)
            self.browser.close()














if __name__ == '__main__':
    unittest.main(verbosity=5)

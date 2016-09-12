#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 07/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import unittest, config
from selenium import webdriver


#Init_block
Init_links = config.GetSettings()
Init_connection = config.GetSettings().get_all_parameters()

#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')

#links
members           = Init_links.get_link("members")
members_group     = Init_links.get_link("members_group")



class Test_loyality_members(unittest.TestCase):
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


    # @unittest.skip('skipped')
    def test_detailed_info_member_positive(self):
        self.Authorize()
        self.browser.get(members)
        member_link = self.browser.find_element_by_xpath('//tr[1]/td[2]/a').get_attribute('href')
        self.browser.get(member_link)
        SearchElement = self.browser.find_element_by_id('cards')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

    # @unittest.skip('skipped')
    def test_detailed_info_members_group_positive(self):
        self.Authorize()
        self.browser.get(members_group)
        members_group_link = self.browser.find_element_by_xpath('//tr[1]/td[2]/a').get_attribute('href')
        self.browser.get(members_group_link)
        SearchElement = self.browser.find_element_by_id('name')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

    # @unittest.skip('skipped')
    def test_members_group_positive(self):
        self.Authorize()
        self.browser.get(members_group)
        SearchElement = self.browser.find_element_by_link_text('VIP')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=5)

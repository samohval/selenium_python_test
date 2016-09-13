#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 05/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import unittest,config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# testSuite
class Test_Loyalty_Authorization_Links(unittest.TestCase):


    def setUp(self):
        self.browser        = webdriver.Firefox()
        self.myBrowser      = config.MyBrowser()
        self.settings       = config.GetSettings()
        self.cards          = self.settings.get_link("cards")
        self.members        = self.settings.get_link("members")
        self.bonus_model    = self.settings.get_link("bonus_model")
        self.trade_point    = self.settings.get_link("trade_point")
        self.edit           = self.settings.get_link("edit")
        self.browser.maximize_window()


    def Authorize(self):
        self.myBrowser.connect_auth_server(self.browser)

#check log|pass
    @unittest.skip('not supported')
    def test_Authorization(self):
        self.Authorize()
        today = self.browser.find_element_by_id("for-today")
        self.assertIn('Loyality', self.browser.title)
        self.assertIsNotNone(today)
        self.browser.close()

#check link cards
    # @unittest.skip('not supported')
    def test_link_Cards_positive(self):
        self.Authorize()
        self.browser.get(self.cards)
        SearchElement = self.browser.find_element_by_id('download')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link members
    # @unittest.skip('not supported')
    def test_link_members_positive(self):
        self.Authorize()
        self.browser.get(self.members)
        SearchElement = self.browser.find_element_by_id('block-member')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link bonus_model
    # @unittest.skip('not supported')
    def test_link_bonus_model_positive(self):
        self.Authorize()
        self.browser.get(self.bonus_model)
        SearchElement = self.browser.find_element_by_id('filter-status')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link trade_point
    # @unittest.skip('not supported')
    def test_link_trade_point_positive(self):
        self.Authorize()
        self.browser.get(self.trade_point)
        SearchElement = self.browser.find_element_by_class_name('text-info')
        self.assertIsNotNone(SearchElement)
        self.browser.close()

#check link edit
    # @unittest.skip('not supported')
    def test_link_edit_positive(self):
        self.Authorize()
        driver = self.browser
        driver.get(self.edit)
        wait = WebDriverWait(driver,5)
        page_loaded = wait.until(lambda driver: driver.find_element_by_id('bonus_auto'))
        self.assertIsNotNone(page_loaded)
        self.browser.close()


    def tearDown(self):

        self.browser.close()
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

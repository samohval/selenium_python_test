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
users = Init_links.get_link("users")
settings = Init_links.get_link("settings")
lbonuses = Init_links.get_link("lbonuses")
obmen = Init_links.get_link("obmen")
setup_models = Init_links.get_link("setup_models")
remove_bon = Init_links.get_link("remove_bon")


#vars
element_demo = "//tr[7]/td[2]/a"
element_id = "login"
_table = ".//*[@id='locked-bonuses-list']"
buttonSearchID = "initial-filling"
modelDBounce = "model_day_bonuses"
Select_buttonName = "card_type_id"

class Test_Loyality_settings(unittest.TestCase):

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

    # @unittest.skip('skipped')
    def test_uses_settings_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(users)
        link_demo = driver.find_element_by_xpath(element_demo).get_attribute('href')
        driver.get(link_demo)
        username = driver.find_element_by_id('nnn').get_attribute('value')
        self.assertEqual(username,'demo','values not equal')
        driver.close()
    # @unittest.skip('skipped')
    def test_settings_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(settings)
        login_text = driver.find_element_by_id(element_id).get_attribute('value')
        self.assertEqual(login_text,'demo', 'login is not DEMO')
        driver.close()

    def test_lbonuses_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(lbonuses)
        tableSearch = driver.find_element_by_xpath(_table)
        self.assertIsNotNone(tableSearch)
        driver.close()

    def test_obmen_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(obmen)
        ButtonSearch = driver.find_element_by_id(buttonSearchID)
        self.assertIsNotNone(ButtonSearch)
        driver.close()

    def test_acc_models_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(setup_models)
        ButtonSearch = driver.find_element_by_name(modelDBounce)
        self.assertIsNotNone(ButtonSearch)
        driver.close()

    def test_remove_bon_positive(self):
        driver = self.browser
        self.Authorize()
        driver.get(remove_bon)
        ButtonSearch = driver.find_element_by_name(Select_buttonName)
        self.assertIsNotNone(ButtonSearch)
        driver.close()



    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

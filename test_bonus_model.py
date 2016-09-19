#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 08/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"


import unittest,datetime,config,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#vars
TEST_MODEL_NAME = 'TEST_MODEL '+str(datetime.datetime.now())
now_date = datetime.date.today()
cur_day = now_date.day

class Test_Loyality_bonus_models(unittest.TestCase):

    def setUp(self):
        self.browser        = webdriver.Firefox()
        self.myBrowser      = config.MyBrowser()
        self.settings       = config.GetSettings()
        self.bonus_model    = self.settings.get_link("bonus_model")
        self.coupons        = self.settings.get_link("coupons")
        self.model_add      = self.bonus_model + self.settings.get_end_of_link("model_add")
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)

    def Authorize(self):
        self.myBrowser.connect_auth_server(self.browser)

    # @unittest.skip('not supported')
    def test_coupons_positive(self):
        self.Authorize()
        driver = self.browser
        driver.get(self.coupons)
        SearchElement = driver.find_element_by_id('lists')
        self.assertIsNotNone(SearchElement)
        driver.close()

    # @unittest.skip('not supported')
    def test_open_model_positive(self):
        self.Authorize()
        driver = self.browser
        driver.get(self.bonus_model)
        model_link = driver.find_element_by_xpath('//tr[1]/td[1]/a').get_attribute('href')
        driver.get(model_link)
        Element = driver.find_element_by_id('remove_restriction')
        self.assertIsNotNone(Element)
        self.browser.close()

    # @unittest.skip('not supported')
    # новая модель добавляется успешно
    def test_add_save_new_model_positive(self):
        self.Authorize()
        driver = self.browser
        wait = WebDriverWait(driver, 15)
        driver.get(self.model_add)
        driver.find_element_by_id('model_name').clear()
        driver.find_element_by_id('model_name').send_keys(TEST_MODEL_NAME)
        driver.find_element_by_id("first_start_day").click()
        driver.find_element_by_link_text(str(cur_day)).click()
        driver.find_element_by_id("first_end_day").click()
        driver.find_element_by_link_text(str(cur_day)).click()
        driver.find_element_by_link_text(u"Выбрать").click()
        driver.find_element_by_name("add-products-id").click()
        driver.find_element_by_xpath("(//input[@name='add-products-id'])[2]").click()
        driver.find_element_by_css_selector("#products-load-buttons > button.btn.btn-primary").click()
        wait.until(lambda driver: driver.find_element_by_id("save"))
        driver.find_element_by_id("save").click()
        wait.until(EC.invisibility_of_element_located((By.ID,'loading')))
        self.assertTrue("/edit/id/" in driver.current_url)
        driver.close()


    def tearDown(self):
        self.browser.close()
        self.browser.quit()



if __name__ == '__main__':
    unittest.main(verbosity=5)

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


Init_links = config.GetSettings()
Init_connection = config.GetSettings().get_all_parameters()

#vars
TEST_MODEL_NAME = 'TEST_MODEL '+str(datetime.datetime.now())
now_date = datetime.date.today()
cur_day = now_date.day


#authorization
srv = Init_connection.get('server')
user = Init_connection.get('user')
pswd = Init_connection.get('password')

#links
bonus_model = Init_links.get_link("bonus_model")
coupons     = Init_links.get_link("coupons")
model_add = bonus_model + Init_links.get_end_of_link("model_add")

class Test_Loyality_bonus_models(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(30)
        self.verificationErrors = []

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
        driver = self.browser
        driver.get(coupons)
        SearchElement = driver.find_element_by_id('lists')
        self.assertIsNotNone(SearchElement)
        driver.close()

    # @unittest.skip('not supported')
    def test_open_model_positive(self):
        self.Authorize()
        driver = self.browser
        driver.get(bonus_model)
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
        driver.get(model_add)
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
        driver.find_element_by_id('save').click()
        driver.save_screenshot('firefox_before_click.png')
        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.invisibility_of_element_located((By.ID,'loading')))
        driver.save_screenshot('firefox_after.click.png')
        self.assertTrue("/edit/id/" in driver.current_url)
        print driver.current_url
        driver.close()

    @unittest.skip('not supported')
    # проверить что изменённая модель отображается в списке моделей
    # тест не окончен!
    def test_modified_model_visible_in_list_positive(self):
        self.Authorize()
        driver = self.browser
        driver.get(bonus_model)
        self.assertTrue("/edit/id/" in driver.current_url)
        driver.close()

    def tearDown(self):
        self.assertEqual([],self.verificationErrors)
        self.browser.close()
        self.browser.quit()



if __name__ == '__main__':
    unittest.main(verbosity=5)

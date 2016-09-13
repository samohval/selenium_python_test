#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 07/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import ConfigParser
from selenium import webdriver

_CONF_FILE = "/home/samohval/Dropbox/GIT/python_selenium_loyality/test.cfg"
conf = ConfigParser.RawConfigParser()
conf.read(_CONF_FILE)



class GetSettings(object):

    def get_link(self,link_id="cards"):
        link = self.get_server() + conf.get("links",link_id)
        return link
    def get_end_of_link(self,link_id="empty"):
        link = conf.get("links",link_id)
        return link
    def get_server(self):
        return conf.get("connection","srv")
    def get_user(self):
        return conf.get("connection","user")
    def get_password(self):
            return conf.get("connection","pass")
    def get_all_parameters(self):
        params = dict(server = self.get_server(),user = self.get_user(),password = self.get_password())
        return params

class MyBrowser(object):

    def __init__(self):
        self.base_url = GetSettings().get_all_parameters().get("server")
        self.settings = GetSettings()

    def main(self):
        print "server base_url: -> " + self.base_url

    def connect_auth_server(self,driver = None):
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(self.settings.get_user())
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.settings.get_password())
        driver.find_element_by_css_selector("#login > #login").click()




if __name__ == '__main__':
    MyBrowser().main()

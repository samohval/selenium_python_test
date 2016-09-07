#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 07/09/2016

__version__ = "0.1"
__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"

import ConfigParser

_CONF_FILE = "/home/samohval/Dropbox/GIT/python_selenium_loyality/test.cfg"
conf = ConfigParser.RawConfigParser()
conf.read(_CONF_FILE)

class GetSettings(object):

    def get_link(self,link_id="cards"):
        try:
            link = self.get_server() + conf.get("links",link_id)
        except Exception as e:
            raise
        else:
            pass
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


if __name__ == '__main__':
    print 'main module'

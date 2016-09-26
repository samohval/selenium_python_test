#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 26-09-2016

__author__ = "Samohval Maxim  <maxim.samohval@protonmail.com>"
__version__ = "0.1"

import unittest
import os
import datetime
import test_authorization_links
import test_check_module_cards
import test_members
import test_bonus_model
import test_directory
import test_settings
import HTMLTestRunner

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_authorization_links)
suite.addTest(loader.loadTestsFromModule(test_check_module_cards))
suite.addTest(loader.loadTestsFromModule(test_members))
suite.addTest(loader.loadTestsFromModule(test_bonus_model))
suite.addTest(loader.loadTestsFromModule(test_directory))
suite.addTest(loader.loadTestsFromModule(test_settings))

dir = os.getcwd()
print (dir)
outfile = open(dir + "/SmokeTestReport_" + str(datetime.datetime.now()) + "_.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, verbosity=2, title="Test_Report", description="SmokeTest")
runner.run(suite)

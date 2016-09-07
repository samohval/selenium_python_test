#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 05/09/2016
# Testing server of Loyality
#add comment

import unittest
import test_authorization_links
import test_check_module_cards

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_authorization_links)
suite.addTest(loader.loadTestsFromModule(test_check_module_cards))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

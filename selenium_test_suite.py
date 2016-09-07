#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: maxim.samohval@protonmail.com
# date: 05/09/2016
# Testing server of Loyality
#add comment

import unittest
import test_authorization_links

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_authorization_links)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

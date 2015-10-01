#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clients
----------------------------------

Tests for `{{ cookiecutter.package_name }}.clients` module.
"""

import unittest

from {{ cookiecutter.package_name }}.clients import {{ cookiecutter.package_name }}Service


class Test{{ cookiecutter.package_name|capitalize }}Service(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

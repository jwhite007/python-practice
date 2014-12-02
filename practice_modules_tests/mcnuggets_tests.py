#! /usr/bin/env python

import unittest
from practice_modules.mcnuggets import mcnuggets


class Test_mcnuggets(unittest.TestCase):
    for i in xrange(1, 110):
        if mcnuggets(i) is not False:

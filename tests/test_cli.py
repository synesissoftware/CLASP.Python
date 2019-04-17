#!/usr/bin/env python

import pyclasp as clasp

import unittest

from StringIO import StringIO

class Util_tester(unittest.TestCase):

    def test_show_version_1(self):

        stm     =   StringIO()

        try:
            specifications =   ()

            clasp.show_version(specifications, version = "1.2.3", stream = stm, program_name = 'myprog', version_prefix = 'v')

            self.assertEqual('myprog v1.2.3', stm.getvalue().strip())

        finally:
            stm.close()


    def test_show_version_2(self):

        stm     =   StringIO()

        try:
            specifications =   ()

            clasp.show_version(specifications, version = [ 1, 2, 3 ], stream = stm, program_name = 'myprog', version_prefix = 'v')

            self.assertEqual('myprog v1.2.3', stm.getvalue().strip())

        finally:
            stm.close()


    def test_show_version_3(self):

        stm     =   StringIO()

        try:
            specifications =   ()

            clasp.show_version(specifications, version = "1.2.3", stream = stm, program_name = 'myprog')

            self.assertEqual('myprog 1.2.3', stm.getvalue().strip())

        finally:
            stm.close()




if '__main__' == __name__:

    unittest.main()



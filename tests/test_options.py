#! /usr/bin/env python

from pyclasp import Arguments
from pyclasp import specification, option
from pyclasp import Flag
from pyclasp import Option
import pyclasp as clasp

import unittest

class Options_tester_1(unittest.TestCase):

    def test_option_with_given_value_in_same_argument(self):

        values_range    =   (

            'silent',
            'normal',
            'verbose',
        )
        option_verbose    =   clasp.option('--verbose', alias = '-v', values_range=values_range, default_value='normal')

        specifications =   (

            option_verbose,
        )
        argv    =   ( 'myprog', '--verbose=silent' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertFalse(args.flags)
        self.assertTrue(args.options)
        self.assertFalse(args.values)

        option  =   args.options[0]

        self.assertEqual('silent', option.value)

    def _test_option_with_given_value_in_separate_argument(self):

        values_range    =   (

            'silent',
            'normal',
            'verbose',
        )
        option_verbose    =   clasp.option('--verbose', alias = '-v', values_range=values_range, default_value='normal')

        specifications =   (

            option_verbose,
        )
        argv    =   ( 'myprog', '--verbose', 'silent' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertFalse(args.flags)
        self.assertTrue(args.options)
        self.assertFalse(args.values)

        option  =   args.options[0]

        self.assertEqual('silent', option.value)

    def test_option_with_empty_value(self):

        values_range    =   (

            'silent',
            'normal',
            'verbose',
        )
        option_verbose    =   clasp.option('--verbose', alias = '-v', values_range=values_range, default_value='normal')

        specifications =   (

            option_verbose,
        )
        argv    =   ( 'myprog', '--verbose=' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertFalse(args.flags)
        self.assertTrue(args.options)
        self.assertFalse(args.values)

        option  =   args.options[0]

        self.assertEqual('normal', option.value)

    def test_option_with_no_given_value(self):

        values_range    =   (

            'silent',
            'normal',
            'verbose',
        )
        option_verbose    =   clasp.option('--verbose', alias = '-v', values_range=values_range, default_value='normal')

        specifications =   (

            option_verbose,
        )
        argv    =   ( 'myprog', '--verbose' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertFalse(args.flags)
        self.assertTrue(args.options)
        self.assertFalse(args.values)

        option  =   args.options[0]

        self.assertEqual('normal', option.value)




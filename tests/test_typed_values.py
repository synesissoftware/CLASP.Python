#! /usr/bin/env python3

# ######################################################################## #
# File:     tests/test_typed_values.py
#
# Purpose:  Tests use of `value_type` with option specifications.
#
# Created:  25th April 2019
# Updated:  27th July 2026
#
# Copyright (c) Matthew Wilson, Synesis Information Systems Pty Ltd
# All rights reserved
#
# ######################################################################## #


from pyclasp import Arguments
from pyclasp import specification, option
from pyclasp import Flag
from pyclasp import Option
import pyclasp as clasp

import unittest

import sys

class Typed_values_tester_1(unittest.TestCase):

    def test_valid_option_value_of_type_str(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=str),
        )

        argv    =   ( "myprog", "--length=1.23", "-l", "4.56", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("--length", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("length", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("1.23", option.given_value)
        self.assertIsInstance(option.value, str)
        self.assertEqual("--length=1.23", str(option))
        self.assertEqual("--length=1.23", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("-l", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("l", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("4.56", option.given_value)
        self.assertIsInstance(option.value, str)
        self.assertEqual("--length=4.56", str(option))
        self.assertEqual("--length=4.56", option)


    def test_valid_option_value_of_type_bool(self):

        specifications =   (

            clasp.option("--verbose", alias="-v", value_type=bool),
        )

        argv    =   ( "myprog", "--verbose=true", "-v", "FALSE", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("--verbose", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("verbose", option.given_label)
        self.assertEqual("--verbose", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("true", option.given_value)
        self.assertIsInstance(option.value, bool)
        self.assertEqual(True, option.value)
        self.assertEqual("--verbose=true", str(option))
        self.assertEqual("--verbose=true", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("-v", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("v", option.given_label)
        self.assertEqual("--verbose", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("FALSE", option.given_value)
        self.assertIsInstance(option.value, bool)
        self.assertEqual(False, option.value)
        self.assertEqual("--verbose=false", str(option))
        self.assertEqual("--verbose=false", option)


    def test_valid_option_value_of_type_float(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=float),
        )

        argv    =   ( "myprog", "--length=1.23", "-l", "4.56", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("--length", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("length", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("1.23", option.given_value)
        self.assertIsInstance(option.value, float)
        self.assertAlmostEqual(1.23, option.value)
        self.assertEqual("--length=1.23", str(option))
        self.assertEqual("--length=1.23", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("-l", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("l", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("4.56", option.given_value)
        self.assertIsInstance(option.value, float)
        self.assertAlmostEqual(4.56, option.value)
        self.assertEqual("--length=4.56", str(option))
        self.assertEqual("--length=4.56", option)


    def test_valid_option_value_of_type_int(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "--length=123", "-l", "456", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("--length", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("length", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("123", option.given_value)
        self.assertIsInstance(option.value, int)
        self.assertEqual(123, option.value)
        self.assertEqual("--length=123", str(option))
        self.assertEqual("--length=123", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("-l", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("l", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("456", option.given_value)
        self.assertIsInstance(option.value, int)
        self.assertEqual(456, option.value)
        self.assertEqual("--length=456", str(option))
        self.assertEqual("--length=456", option)


    if sys.version_info < (3, 0):

        def test_valid_option_value_of_type_long(self):

            specifications =   (

                clasp.option("--length", alias="-l", value_type=long),
            )

            argv    =   ( "myprog", "--length=123", "-l", "456", )
            args    =   clasp.parse(argv, specifications)

            self.assertEqual(0, len(args.flags))
            self.assertEqual(2, len(args.options))
            self.assertEqual(0, len(args.values))

            option  =   args.options[0]

            self.assertIsInstance(option, ( Option, ))
            self.assertEqual(1, option.given_index)
            self.assertEqual("--length", option.given_name)
            self.assertTrue(option.argument_specification)
            self.assertEqual(2, option.given_hyphens)
            self.assertEqual("length", option.given_label)
            self.assertEqual("--length", option.name)
            self.assertEqual({}, option.extras)
            self.assertEqual("123", option.given_value)
            self.assertIsInstance(option.value, long)
            self.assertEqual(123, option.value)
            self.assertEqual("--length=123", str(option))
            self.assertEqual("--length=123", option)

            option  =   args.options[1]

            self.assertIsInstance(option, ( Option, ))
            self.assertEqual(2, option.given_index)
            self.assertEqual("-l", option.given_name)
            self.assertTrue(option.argument_specification)
            self.assertEqual(1, option.given_hyphens)
            self.assertEqual("l", option.given_label)
            self.assertEqual("--length", option.name)
            self.assertEqual({}, option.extras)
            self.assertEqual("456", option.given_value)
            self.assertIsInstance(option.value, long)
            self.assertEqual(456, option.value)
            self.assertEqual("--length=456", str(option))
            self.assertEqual("--length=456", option)


    def test_invalid_option_value_of_type_int(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "--length=abc" )

        with self.assertRaises(clasp.InvalidIntegerException):

            clasp.parse(argv, specifications)


    def test_invalid_option_value_of_type_float(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=float),
        )

        argv    =   ( "myprog", "--length=abc" )

        with self.assertRaises(clasp.InvalidNumberException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "--length=" )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_2(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "-l" )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_3(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "--length" )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_4(self):

        specifications =   (

            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "--length", "--" )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_invalid_option_value_of_type_that_is_not_supported(self):

        with self.assertRaises(TypeError):

            clasp.option("--length", alias="-l", value_type="abc"),


    def test_flags_of_flags_and_options_combined(self):

        specifications =   (

            clasp.flag("--compile", alias="-c"),
            clasp.flag("--mode=debug", alias="-d"),
            clasp.flag("--execute", alias="-e"),
            clasp.option("--mode", alias="-m"),
            clasp.option("--length", alias="-l", value_type=int),
        )

        argv    =   ( "myprog", "-ced", "-l", "123" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertTrue(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--compile", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--compile", str(flag))
        self.assertEqual("--compile", flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertTrue(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--execute", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--execute", str(flag))
        self.assertEqual("--execute", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-ced", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("ced", option.given_label)
        self.assertEqual("--mode", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("debug", option.given_value)
        self.assertEqual("debug", option.value)
        self.assertEqual("--mode=debug", str(option))
        self.assertEqual("--mode=debug", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("-l", option.given_name)
        self.assertTrue(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("l", option.given_label)
        self.assertEqual("--length", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("123", option.given_value)
        self.assertEqual(123, option.value)
        self.assertEqual("--length=123", str(option))
        self.assertEqual("--length=123", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))



if '__main__' == __name__:

    unittest.main()



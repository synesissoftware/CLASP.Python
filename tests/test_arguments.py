#! /usr/bin/env python3

# ######################################################################## #
# File:     tests/test_arguments.py
#
# Purpose:  Tests a large variety of command-line arguments.
#
# Created:  14th February 2019
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

class Arguments_tester_1(unittest.TestCase):


    def test_empty_args_via_clasp_parse(self):

        argv    =   ()

        with self.assertRaises(IndexError):

            clasp.parse(argv)


    def test_no_args_via_clasp_parse(self):

        argv    =   ( "myprog", )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_no_args_via_Arguments_constructor(self):

        argv    =   ( "myprog", )
        args    =   Arguments(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_value(self):

        argv    =   ( "myprog", "value1", )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))


    def test_two_values(self):

        argv    =   ( "myprog", "value1", "value2" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)


    def test_ten_values(self):

        argv    =   [ "myprog", ] + [ "value%d" % i for i in range(0, 10) ]
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)
        self.assertEqual(10, len(args.values))


    def test_one_flag(self):

        argv    =   ( "myprog", "-f1", )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))


    def test_two_flags(self):

        argv    =   ( "myprog", "-f1", "--flag2" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(2, flag.given_index)
        self.assertEqual("--flag2", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(2, flag.given_hyphens)
        self.assertEqual("flag2", flag.given_label)
        self.assertEqual("--flag2", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--flag2", str(flag))
        self.assertEqual("--flag2", flag)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_three_flags(self):

        argv    =   ( "myprog", "-f1", "--flag2", "---x" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(2, flag.given_index)
        self.assertEqual("--flag2", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(2, flag.given_hyphens)
        self.assertEqual("flag2", flag.given_label)
        self.assertEqual("--flag2", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--flag2", str(flag))
        self.assertEqual("--flag2", flag)

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(3, flag.given_index)
        self.assertEqual("---x", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(3, flag.given_hyphens)
        self.assertEqual("x", flag.given_label)
        self.assertEqual("---x", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("---x", str(flag))
        self.assertEqual("---x", flag)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_option(self):

        argv    =   ( "myprog", "-o1=v1", )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o1", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o1", option.given_label)
        self.assertEqual("-o1", option.name)
        self.assertEqual("v1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("-o1=v1", str(option))
        self.assertEqual("-o1=v1", option)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_two_options(self):

        argv    =   ( "myprog", "-o1=v1", "--option2=value2" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o1", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o1", option.given_label)
        self.assertEqual("-o1", option.name)
        self.assertEqual("v1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("-o1=v1", str(option))
        self.assertEqual("-o1=v1", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("--option2", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("option2", option.given_label)
        self.assertEqual("--option2", option.name)
        self.assertEqual("value2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option2=value2", str(option))
        self.assertEqual("--option2=value2", option)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_three_options(self):

        argv    =   ( "myprog", "-o1=v1", "--option2=value2", "---the-third-option=the third value" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o1", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o1", option.given_label)
        self.assertEqual("-o1", option.name)
        self.assertEqual("v1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("-o1=v1", str(option))
        self.assertEqual("-o1=v1", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(2, option.given_index)
        self.assertEqual("--option2", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("option2", option.given_label)
        self.assertEqual("--option2", option.name)
        self.assertEqual("value2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option2=value2", str(option))
        self.assertEqual("--option2=value2", option)

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("---the-third-option", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(3, option.given_hyphens)
        self.assertEqual("the-third-option", option.given_label)
        self.assertEqual("---the-third-option", option.name)
        self.assertEqual("the third value", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("---the-third-option=the third value", str(option))
        self.assertEqual("---the-third-option=the third value", option)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_flag_and_one_option_and_one_value(self):

        argv    =   ( "myprog", "-f1", "value1", "--first-option=val1" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option    =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("--first-option", option.given_name)
        self.assertIsNone(option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("first-option", option.given_label)
        self.assertEqual("--first-option", option.name)
        self.assertEqual("val1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--first-option=val1", str(option))
        self.assertEqual("--first-option=val1", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value1", args.values[0])


    def test_double_hyphen_1(self):

        argv    =   ( "myprog", "-f1", "value1", "--", "-f2" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(2, len(args.values))

        self.assertEqual("value1", args.values[0])
        self.assertEqual("-f2", args.values[1])


    def test_double_hyphen_2(self):

        argv    =   ( "myprog", "-f1", "value1", "--", "-f2", "--", "--option1=v1" )
        args    =   clasp.parse(argv)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(4, len(args.values))

        self.assertEqual("value1", args.values[0])
        self.assertEqual("-f2", args.values[1])
        self.assertEqual("--", args.values[2])
        self.assertEqual("--option1=v1", args.values[3])


    def test_one_flag_and_one_option_and_one_value_with_empty_specifications(self):

        specifications_list    =   ( tuple(), list(), None )

        for specifications in specifications_list:

            argv    =   ( "myprog", "-f1", "value1", "--first-option=val1" )
            args    =   clasp.parse(argv, specifications)

            self.assertEqual("myprog", args.program_name)

            self.assertIsInstance(args.flags, ( tuple, ))
            self.assertTrue(args.flags)
            self.assertEqual(1, len(args.flags))

            flag    =   args.flags[0]

            self.assertIsInstance(flag, ( Flag, ))
            self.assertEqual(1, flag.given_index)
            self.assertEqual("-f1", flag.given_name)
            self.assertIsNone(flag.argument_specification)
            self.assertEqual(1, flag.given_hyphens)
            self.assertEqual("f1", flag.given_label)
            self.assertEqual("-f1", flag.name)
            self.assertEqual({}, flag.extras)
            self.assertEqual("-f1", str(flag))
            self.assertEqual("-f1", flag)

            self.assertIsInstance(args.options, ( tuple, ))
            self.assertTrue(args.options)
            self.assertEqual(1, len(args.options))

            option    =   args.options[0]

            self.assertIsInstance(option, ( Option, ))
            self.assertEqual(3, option.given_index)
            self.assertEqual("--first-option", option.given_name)
            self.assertIsNone(option.argument_specification)
            self.assertEqual(2, option.given_hyphens)
            self.assertEqual("first-option", option.given_label)
            self.assertEqual("--first-option", option.name)
            self.assertEqual("val1", option.value)
            self.assertEqual({}, option.extras)
            self.assertEqual("--first-option=val1", str(option))
            self.assertEqual("--first-option=val1", option)

            self.assertIsInstance(args.values, ( tuple, ))
            self.assertTrue(args.values)
            self.assertEqual(1, len(args.values))

            self.assertEqual("value1", args.values[0])


    def test_alias_of_flag_with_one_specification(self):

        flag_verbose    =   clasp.flag("--verbose", alias = "-v", extras = { "x-name": "v-val" })

        specifications =   (

            flag_verbose,
        )
        argv    =   ( "myprog", "--verbose", "--succinct", "value", "-v" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(4, flag.given_index)
        self.assertEqual("-v", flag.given_name)
        self.assertEqual(flag_verbose, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("v", flag.given_label)
        self.assertEqual("--verbose", flag.name)
        self.assertEqual({ "x-name": "v-val" }, flag.extras)
        self.assertEqual("--verbose", str(flag))
        self.assertEqual("--verbose", flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(2, flag.given_index)
        self.assertEqual("--succinct", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(2, flag.given_hyphens)
        self.assertEqual("succinct", flag.given_label)
        self.assertEqual("--succinct", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--succinct", str(flag))
        self.assertEqual("--succinct", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value", args.values[0])


    def test_alias_of_flag_with_two_specifications(self):

        flag_expand =   clasp.flag("--expand", aliases = ( "-x", "--x", ), extras = { "some-value": ( "e", "x", "t", "r", "a", "s", ) })

        specifications =   (

            flag_expand,
        )
        argv    =   ( "myprog", "-f1", "value1", "-x", "--delete", "--x", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(5, flag.given_index) # 5 not 3, because the second instance overrides the first
        self.assertEqual("--x", flag.given_name)
        self.assertEqual(flag_expand, flag.argument_specification)
        self.assertEqual(2, flag.given_hyphens)
        self.assertEqual("x", flag.given_label)
        self.assertEqual("--expand", flag.name)
        self.assertTrue(flag.extras)
        self.assertEqual("--expand", str(flag))
        self.assertEqual("--expand", flag)

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(4, flag.given_index)
        self.assertEqual("--delete", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(2, flag.given_hyphens)
        self.assertEqual("delete", flag.given_label)
        self.assertEqual("--delete", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--delete", str(flag))
        self.assertEqual("--delete", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value1", args.values[0])


    def test_alias_of_option_with_one_specification(self):

        option_option   =   clasp.option("--option", alias = "-o")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-f1", "value1", "-o=value2", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(option_option, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("value2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=value2", str(option))
        self.assertEqual("--option=value2", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value1", args.values[0])


    def test_alias_of_option_with_separate_value(self):

        option_option   =   clasp.option("--option", alias = "-o")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-o", "value-1", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(option_option, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("value-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=value-1", str(option))
        self.assertEqual("--option=value-1", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_separate_value(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "def-val-1")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-o", "value-1", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(option_option, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("value-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=value-1", str(option))
        self.assertEqual("--option=value-1", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_separate_value_that_resembles_flag(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "def-val-1")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-o", "-o", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(option_option, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("-o", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=-o", str(option))
        self.assertEqual("--option=-o", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_missing_separate_value(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "def-val-1")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-o", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(option_option, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("def-val-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=def-val-1", str(option))
        self.assertEqual("--option=def-val-1", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_with_attached_empty(self):

        specifications =   (

            clasp.option("--option", alias = "-o", default_value = "def-val-1"),
        )
        argv    =   ( "myprog", "-o=", "value-2", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("def-val-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=def-val-1", str(option))
        self.assertEqual("--option=def-val-1", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value-2", args.values[0])


    def test_flag_alias_of_option_with_value(self):

        option_verbosity    =   clasp.option("--verbosity")

        specifications =   (

            option_verbosity,
            clasp.flag("--verbosity=high", alias = "-v"),
        )
        argv    =   ( "myprog", "-v", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-v", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("v", option.given_label)
        self.assertEqual("--verbosity", option.name)
        self.assertEqual("high", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--verbosity=high", str(option))
        self.assertEqual("--verbosity=high", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_with_value_allowing_multiple(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="allow")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-f1", "value-1", "-o=", "-o=given-value-1", "--option=given-value-2", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))


        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("default-value", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=default-value", str(option))
        self.assertEqual("--option=default-value", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(4, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-1", str(option))
        self.assertEqual("--option=given-value-1", option)

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(5, option.given_index)
        self.assertEqual("--option", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("option", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-2", str(option))
        self.assertEqual("--option=given-value-2", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value-1", args.values[0])

    def test_alias_of_option_with_value_ignoring_multiple(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="ignore")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-f1", "value-1", "-o=", "-o=given-value-1", "--option=given-value-2", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))


        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("default-value", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=default-value", str(option))
        self.assertEqual("--option=default-value", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(4, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-1", str(option))
        self.assertEqual("--option=given-value-1", option)

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(5, option.given_index)
        self.assertEqual("--option", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("option", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-2", str(option))
        self.assertEqual("--option=given-value-2", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value-1", args.values[0])

    def test_alias_of_option_with_value_replacing_multiple(self):

        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="replace")

        specifications =   (

            option_option,
        )
        argv    =   ( "myprog", "-f1", "value-1", "-o=", "-o=given-value-1", "--option=given-value-2", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))


        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-f1", flag.given_name)
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("f1", flag.given_label)
        self.assertEqual("-f1", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("-f1", str(flag))
        self.assertEqual("-f1", flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(3, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("default-value", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=default-value", str(option))
        self.assertEqual("--option=default-value", option)

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(4, option.given_index)
        self.assertEqual("-o", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("o", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-1", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-1", str(option))
        self.assertEqual("--option=given-value-1", option)

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(5, option.given_index)
        self.assertEqual("--option", option.given_name)
        self.assertEqual(specifications[0], option.argument_specification)
        self.assertEqual(2, option.given_hyphens)
        self.assertEqual("option", option.given_label)
        self.assertEqual("--option", option.name)
        self.assertEqual("given-value-2", option.value)
        self.assertEqual({}, option.extras)
        self.assertEqual("--option=given-value-2", str(option))
        self.assertEqual("--option=given-value-2", option)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual("value-1", args.values[0])

    def test_flags_combined(self):

        flag_compile    =   clasp.flag("--compile", alias = "-c")
        flag_debug      =   clasp.flag("--debug", alias = "-d")
        flag_execute    =   clasp.flag("--execute", alias = "-e")

        specifications =   (

            flag_compile,
            flag_debug,
            flag_execute,
        )

        self.assertEqual(flag_compile, specifications[0])
        self.assertEqual(flag_debug, specifications[1])
        self.assertEqual(flag_execute, specifications[2])

        argv    =   ( "myprog", "-ced", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertEqual(flag_compile, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--compile", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--compile", str(flag))
        self.assertEqual("--compile", flag)
        self.assertTrue(flag == flag_compile)
        self.assertEqual(flag_compile, flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertEqual(flag_execute, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--execute", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--execute", str(flag))
        self.assertEqual("--execute", flag)
        self.assertTrue(flag == flag_execute)
        self.assertEqual(flag_execute, flag)

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertEqual(flag_debug, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--debug", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--debug", str(flag))
        self.assertEqual("--debug", flag)
        self.assertEqual(flag_debug, flag)
        self.assertTrue(flag == flag_debug)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)
        self.assertEqual(0, len(args.options))

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_flags_of_flags_and_options_combined(self):

        flag_compile    =   clasp.flag("--compile", alias = "-c")
        flag_execute    =   clasp.flag("--execute", alias = "-e")
        option_mode     =   clasp.option("--mode", alias = "-m")

        specifications =   (

            flag_compile,
            clasp.flag("--mode=debug", alias = "-d"),
            flag_execute,
            option_mode,
        )

        argv    =   ( "myprog", "-ced", )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertEqual(flag_compile, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--compile", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--compile", str(flag))
        self.assertEqual("--compile", flag)
        self.assertTrue(flag == flag_compile)
        self.assertEqual(flag_compile, flag)

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(1, flag.given_index)
        self.assertEqual("-ced", flag.given_name)
        self.assertEqual(flag_execute, flag.argument_specification)
        self.assertEqual(1, flag.given_hyphens)
        self.assertEqual("ced", flag.given_label)
        self.assertEqual("--execute", flag.name)
        self.assertEqual({}, flag.extras)
        self.assertEqual("--execute", str(flag))
        self.assertEqual("--execute", flag)
        self.assertTrue(flag == flag_execute)
        self.assertEqual(flag_execute, flag)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(1, option.given_index)
        self.assertEqual("-ced", option.given_name)
        self.assertEqual(option_mode, option.argument_specification)
        self.assertEqual(1, option.given_hyphens)
        self.assertEqual("ced", option.given_label)
        self.assertEqual("--mode", option.name)
        self.assertEqual({}, option.extras)
        self.assertEqual("--mode=debug", str(option))
        self.assertEqual("--mode=debug", option)
        self.assertEqual(option_mode, option)
        self.assertTrue(option == option_mode)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))

    def test_first_unused_Flag_via_get_first_unused_flag(self):

        flag_compile    =   clasp.flag("--compile", alias = "-c")
        flag_debug      =   clasp.flag("--debug", alias = "-d")

        specifications = (

            flag_compile,
            flag_debug,
        )

        argv    =   ( "dir1/myprog", "-cd" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_option())

        # before any use()d

        fu      =   args.get_first_unused_flag()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_compile, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused_flag()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_debug, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused_flag()

        self.assertIsNone(fu)

    def test_first_unused_Flag_via_get_first_unused_flag_or_option(self):

        flag_compile    =   clasp.flag("--compile", alias = "-c")
        flag_debug      =   clasp.flag("--debug", alias = "-d")

        specifications = (

            flag_compile,
            flag_debug,
        )

        argv    =   ( "dir1/myprog", "-cd" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_option())

        # before any use()d

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_compile, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_debug, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNone(fu)

    def test_first_unused_Flag_via_get_first_unused(self):

        flag_compile    =   clasp.flag("--compile", alias = "-c")
        flag_debug      =   clasp.flag("--debug", alias = "-d")

        specifications = (

            flag_compile,
            flag_debug,
        )

        argv    =   ( "dir1/myprog", "-cd" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_option())

        # before any use()d

        fu      =   args.get_first_unused()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_compile, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused()

        self.assertIsNotNone(fu)
        self.assertEqual(flag_debug, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused()

        self.assertIsNone(fu)

    def test_first_unused_Option_via_get_first_unused_option(self):

        option_mode     =   clasp.option("--mode", alias = "-m")
        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="replace")

        specifications = (

            option_mode,
            option_option,
        )

        argv    =   ( "dir1/myprog", "--mode=verbose", "--option=ignore" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_flag())

        # before any use()d

        fu      =   args.get_first_unused_option()

        self.assertIsNotNone(fu)
        self.assertEqual(option_mode, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused_option()

        self.assertIsNotNone(fu)
        self.assertEqual(option_option, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused_option()

        self.assertIsNone(fu)

    def test_first_unused_Option_via_get_first_unused_flag_or_option(self):

        option_mode     =   clasp.option("--mode", alias = "-m")
        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="replace")

        specifications = (

            option_mode,
            option_option,
        )

        argv    =   ( "dir1/myprog", "--mode=verbose", "--option=ignore" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_flag())

        # before any use()d

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNotNone(fu)
        self.assertEqual(option_mode, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNotNone(fu)
        self.assertEqual(option_option, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused_flag_or_option()

        self.assertIsNone(fu)

    def test_first_unused_Option_via_get_first_unused(self):

        option_mode     =   clasp.option("--mode", alias = "-m")
        option_option   =   clasp.option("--option", alias = "-o", default_value = "default-value", on_multiple="replace")

        specifications = (

            option_mode,
            option_option,
        )

        argv    =   ( "dir1/myprog", "--mode=verbose", "--option=ignore" )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual("myprog", args.program_name)

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))


        # now check the "unused", iteratively using and testing

        self.assertIsNone(args.get_first_unused_flag())

        # before any use()d

        fu      =   args.get_first_unused()

        self.assertIsNotNone(fu)
        self.assertEqual(option_mode, fu)

        # after use() (1st time)

        fu.use()

        fu      =   args.get_first_unused()

        self.assertIsNotNone(fu)
        self.assertEqual(option_option, fu)

        # after use() (2nd time)

        fu.use()

        fu      =   args.get_first_unused()

        self.assertIsNone(fu)



if '__main__' == __name__:

    unittest.main()



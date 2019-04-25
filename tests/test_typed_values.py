#!/usr/bin/env python

from pyclasp import Arguments
from pyclasp import specification, option
from pyclasp import Flag
from pyclasp import Option
import pyclasp as clasp

import unittest

class Typed_values_tester_1(unittest.TestCase):

    def test_valid_option_value_of_type_float(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=float),
        )

        argv    =   ( 'myprog', '--length=1.23', '-l', '4.56', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   1)
        self.assertEqual(option.given_name        ,   '--length')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   2)
        self.assertEqual(option.given_label       ,   'length')
        self.assertEqual(option.name              ,   '--length')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   '1.23')
        self.assertAlmostEqual(option.value       ,   1.23)
        self.assertEqual(str(option)              ,   '--length=1.23')
        self.assertEqual(option                   ,   '--length=1.23')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   2)
        self.assertEqual(option.given_name        ,   '-l')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   1)
        self.assertEqual(option.given_label       ,   'l')
        self.assertEqual(option.name              ,   '--length')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   '4.56')
        self.assertAlmostEqual(option.value       ,   4.56)
        self.assertEqual(str(option)              ,   '--length=4.56')
        self.assertEqual(option                   ,   '--length=4.56')


    def test_valid_option_value_of_type_int(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '--length=123', '-l', '456', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual(0, len(args.flags))
        self.assertEqual(2, len(args.options))
        self.assertEqual(0, len(args.values))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   1)
        self.assertEqual(option.given_name        ,   '--length')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   2)
        self.assertEqual(option.given_label       ,   'length')
        self.assertEqual(option.name              ,   '--length')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   '123')
        self.assertEqual(option.value             ,   123)
        self.assertEqual(str(option)              ,   '--length=123')
        self.assertEqual(option                   ,   '--length=123')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   2)
        self.assertEqual(option.given_name        ,   '-l')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   1)
        self.assertEqual(option.given_label       ,   'l')
        self.assertEqual(option.name              ,   '--length')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   '456')
        self.assertEqual(option.value             ,   456)
        self.assertEqual(str(option)              ,   '--length=456')
        self.assertEqual(option                   ,   '--length=456')


    def test_invalid_option_value_of_type_int(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '--length=abc' )

        with self.assertRaises(clasp.InvalidIntegerException):

            clasp.parse(argv, specifications)


    def test_invalid_option_value_of_type_float(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=float),
        )

        argv    =   ( 'myprog', '--length=abc' )

        with self.assertRaises(clasp.InvalidNumberException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '--length=' )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_2(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '-l' )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_3(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '--length' )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_empty_option_value_of_type_int_4(self):

        specifications =   (

            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '--length', '--' )

        with self.assertRaises(clasp.MissingValueException):

            clasp.parse(argv, specifications)


    def test_invalid_option_value_of_type_that_is_not_supported(self):

        with self.assertRaises(TypeError):

            clasp.option('--length', alias='-l', value_type='abc'),


    def test_flags_of_flags_and_options_combined(self):

        specifications =   (

            clasp.flag('--compile', alias='-c'),
            clasp.flag('--mode=debug', alias='-d'),
            clasp.flag('--execute', alias='-e'),
            clasp.option('--mode', alias='-m'),
            clasp.option('--length', alias='-l', value_type=int),
        )

        argv    =   ( 'myprog', '-ced', '-l', '123' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-ced')
        self.assertTrue(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'ced')
        self.assertEqual(flag.name              ,   '--compile')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--compile')
        self.assertEqual(flag                   ,   '--compile')

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-ced')
        self.assertTrue(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'ced')
        self.assertEqual(flag.name              ,   '--execute')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--execute')
        self.assertEqual(flag                   ,   '--execute')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   1)
        self.assertEqual(option.given_name        ,   '-ced')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   1)
        self.assertEqual(option.given_label       ,   'ced')
        self.assertEqual(option.name              ,   '--mode')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   'debug')
        self.assertEqual(option.value             ,   'debug')
        self.assertEqual(str(option)              ,   '--mode=debug')
        self.assertEqual(option                   ,   '--mode=debug')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   2)
        self.assertEqual(option.given_name        ,   '-l')
        self.assertTrue(option.argument_specification)
        self.assertEqual(option.given_hyphens     ,   1)
        self.assertEqual(option.given_label       ,   'l')
        self.assertEqual(option.name              ,   '--length')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(option.given_value       ,   '123')
        self.assertEqual(option.value             ,   123)
        self.assertEqual(str(option)              ,   '--length=123')
        self.assertEqual(option                   ,   '--length=123')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))



if '__main__' == __name__:

    unittest.main()



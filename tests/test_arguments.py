#!/usr/bin/env python

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

        argv    =   ( 'myprog', )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_no_args_via_Arguments_constructor(self):

        argv    =   ( 'myprog', )
        args    =   Arguments(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_value(self):

        argv    =   ( 'myprog', 'value1', )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))


    def test_two_values(self):

        argv    =   ( 'myprog', 'value1', 'value2' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)


    def test_ten_values(self):

        argv    =   [ 'myprog', ] + [ "value%d" % i for i in range(0, 10) ]
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertTrue(args.values)
        self.assertEqual(10, len(args.values))


    def test_one_flag(self):

        argv    =   ( 'myprog', '-f1', )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))


    def test_two_flags(self):

        argv    =   ( 'myprog', '-f1', '--flag2' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   2)
        self.assertEqual(flag.given_name        ,   '--flag2')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'flag2')
        self.assertEqual(flag.name              ,   '--flag2')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--flag2')
        self.assertEqual(flag                   ,   '--flag2')

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_three_flags(self):

        argv    =   ( 'myprog', '-f1', '--flag2', '---x' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   2)
        self.assertEqual(flag.given_name        ,   '--flag2')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'flag2')
        self.assertEqual(flag.name              ,   '--flag2')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--flag2')
        self.assertEqual(flag                   ,   '--flag2')

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   3)
        self.assertEqual(flag.given_name        ,   '---x')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   3)
        self.assertEqual(flag.given_label       ,   'x')
        self.assertEqual(flag.name              ,   '---x')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '---x')
        self.assertEqual(flag                   ,   '---x')

        self.assertIsInstance(args.options, ( tuple ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_option(self):

        argv    =   ( 'myprog', '-o1=v1', )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o1')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o1')
        self.assertEqual(option.name            ,   '-o1')
        self.assertEqual(option.value           ,   'v1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '-o1=v1')
        self.assertEqual(option                 ,   '-o1=v1')

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_two_options(self):

        argv    =   ( 'myprog', '-o1=v1', '--option2=value2' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(2, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o1')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o1')
        self.assertEqual(option.name            ,   '-o1')
        self.assertEqual(option.value           ,   'v1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '-o1=v1')
        self.assertEqual(option                 ,   '-o1=v1')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   2)
        self.assertEqual(option.given_name      ,   '--option2')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   2)
        self.assertEqual(option.given_label     ,   'option2')
        self.assertEqual(option.name            ,   '--option2')
        self.assertEqual(option.value           ,   'value2')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option2=value2')
        self.assertEqual(option                 ,   '--option2=value2')

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_three_options(self):

        argv    =   ( 'myprog', '-o1=v1', '--option2=value2', '---the-third-option=the third value' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple ))
        self.assertFalse(args.flags)

        self.assertIsInstance(args.options, ( tuple ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o1')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o1')
        self.assertEqual(option.name            ,   '-o1')
        self.assertEqual(option.value           ,   'v1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '-o1=v1')
        self.assertEqual(option                 ,   '-o1=v1')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   2)
        self.assertEqual(option.given_name      ,   '--option2')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   2)
        self.assertEqual(option.given_label     ,   'option2')
        self.assertEqual(option.name            ,   '--option2')
        self.assertEqual(option.value           ,   'value2')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option2=value2')
        self.assertEqual(option                 ,   '--option2=value2')

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   3)
        self.assertEqual(option.given_name      ,   '---the-third-option')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   3)
        self.assertEqual(option.given_label     ,   'the-third-option')
        self.assertEqual(option.name            ,   '---the-third-option')
        self.assertEqual(option.value           ,   'the third value')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '---the-third-option=the third value')
        self.assertEqual(option                 ,   '---the-third-option=the third value')

        self.assertIsInstance(args.values, ( tuple ))
        self.assertFalse(args.values)


    def test_one_flag_and_one_option_and_one_value(self):

        argv    =   ( 'myprog', '-f1', 'value1', '--first-option=val1' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option    =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   3)
        self.assertEqual(option.given_name      ,   '--first-option')
        self.assertIsNone(option.argument_specification)
        self.assertEqual(option.given_hyphens   ,   2)
        self.assertEqual(option.given_label     ,   'first-option')
        self.assertEqual(option.name            ,   '--first-option')
        self.assertEqual(option.value           ,   'val1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--first-option=val1')
        self.assertEqual(option                 ,   '--first-option=val1')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value1', args.values[0])


    def test_double_hyphen_1(self):

        argv    =   ( 'myprog', '-f1', 'value1', '--', '-f2' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(2, len(args.values))

        self.assertEqual('value1', args.values[0])
        self.assertEqual('-f2', args.values[1])


    def test_double_hyphen_2(self):

        argv    =   ( 'myprog', '-f1', 'value1', '--', '-f2', '--', '--option1=v1' )
        args    =   clasp.parse(argv)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(4, len(args.values))

        self.assertEqual('value1', args.values[0])
        self.assertEqual('-f2', args.values[1])
        self.assertEqual('--', args.values[2])
        self.assertEqual('--option1=v1', args.values[3])


    def test_one_flag_and_one_option_and_one_value_with_empty_specifications(self):

        specifications_list    =   ( tuple(), list(), None )

        for specifications in specifications_list:

            argv    =   ( 'myprog', '-f1', 'value1', '--first-option=val1' )
            args    =   clasp.parse(argv, specifications)

            self.assertEqual('myprog', args.program_name)

            self.assertIsInstance(args.flags, ( tuple, ))
            self.assertTrue(args.flags)
            self.assertEqual(1, len(args.flags))

            flag    =   args.flags[0]

            self.assertIsInstance(flag, ( Flag, ))
            self.assertEqual(flag.given_index       ,   1)
            self.assertEqual(flag.given_name        ,   '-f1')
            self.assertIsNone(flag.argument_specification)
            self.assertEqual(flag.given_hyphens     ,   1)
            self.assertEqual(flag.given_label       ,   'f1')
            self.assertEqual(flag.name              ,   '-f1')
            self.assertEqual(flag.extras            ,   {})
            self.assertEqual(str(flag)              ,   '-f1')
            self.assertEqual(flag                   ,   '-f1')

            self.assertIsInstance(args.options, ( tuple, ))
            self.assertTrue(args.options)
            self.assertEqual(1, len(args.options))

            option    =   args.options[0]

            self.assertIsInstance(option, ( Option, ))
            self.assertEqual(option.given_index     ,   3)
            self.assertEqual(option.given_name      ,   '--first-option')
            self.assertIsNone(option.argument_specification)
            self.assertEqual(option.given_hyphens   ,   2)
            self.assertEqual(option.given_label     ,   'first-option')
            self.assertEqual(option.name            ,   '--first-option')
            self.assertEqual(option.value           ,   'val1')
            self.assertEqual(option.extras          ,   {})
            self.assertEqual(str(option)            ,   '--first-option=val1')
            self.assertEqual(option                 ,   '--first-option=val1')

            self.assertIsInstance(args.values, ( tuple, ))
            self.assertTrue(args.values)
            self.assertEqual(1, len(args.values))

            self.assertEqual('value1', args.values[0])


    def test_alias_of_flag_with_one_specification(self):

        specifications =   (

            clasp.flag('--verbose', alias = '-v', extras = { 'x-name': 'v-val' }),
        )
        argv    =   ( 'myprog', '--verbose', '--succinct', 'value', '-v' )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '--verbose')
        self.assertEqual(flag.argument_specification, specifications[0])
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'verbose')
        self.assertEqual(flag.name              ,   '--verbose')
        self.assertEqual(flag.extras            ,   { 'x-name': 'v-val' })
        self.assertEqual(str(flag)              ,   '--verbose')
        self.assertEqual(flag                   ,   '--verbose')

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   2)
        self.assertEqual(flag.given_name        ,   '--succinct')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'succinct')
        self.assertEqual(flag.name              ,   '--succinct')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--succinct')
        self.assertEqual(flag                   ,   '--succinct')

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   4)
        self.assertEqual(flag.given_name        ,   '-v')
        self.assertEqual(flag.argument_specification, specifications[0])
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'v')
        self.assertEqual(flag.name              ,   '--verbose')
        self.assertEqual(flag.extras            ,   { 'x-name': 'v-val' })
        self.assertEqual(str(flag)              ,   '--verbose')
        self.assertEqual(flag                   ,   '--verbose')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value', args.values[0])


    def alias_of_flag_with_two_specifications(self):

        specifications =   (

            clasp.flag('--expand', aliases = ( '-x', '--x', ), extras = { 'some-value': ( 'e', 'x', 't', 'r', 'a', 's', ) }),
        )
        argv    =   ( 'myprog', '-f1', 'value1', '-x', '--delete', '--x', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(4, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        flag    =   args.flags[1]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   3)
        self.assertEqual(flag.given_name        ,   '-x')
        self.assertEqual(flag.argument_specification, specifications[0])
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'x')
        self.assertEqual(flag.name              ,   '--expand')
        self.assertTrue(flag.extras)
        self.assertEqual(str(flag)              ,   '--expand')
        self.assertEqual(flag                   ,   '--expand')

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   4)
        self.assertEqual(flag.given_name        ,   '--delete')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'delete')
        self.assertEqual(flag.name              ,   '--delete')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--delete')
        self.assertEqual(flag                   ,   '--delete')

        flag    =   args.flags[3]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   5)
        self.assertEqual(flag.given_name        ,   '--x')
        self.assertEqual(flag.argument_specification, specifications[x])
        self.assertEqual(flag.given_hyphens     ,   2)
        self.assertEqual(flag.given_label       ,   'x')
        self.assertEqual(flag.name              ,   '--expand')
        self.assertTrue(flag.extras)
        self.assertIsInstance(flag.extras, dict)
        self.assertEqual(1, len(flag.extras))
        self.assertEqual(( 'e', 'x', 't', 'r', 'a', 's', ), flag.extras['some-value'])
        self.assertEqual(str(flag)              ,   '--expand')
        self.assertEqual(flag                   ,   '--expand')


        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value1', args.values[0])


    def test_alias_of_option_with_one_specification(self):

        specifications =   (

            clasp.option('--option', alias = '-o'),
        )
        argv    =   ( 'myprog', '-f1', 'value1', '-o=value2', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   3)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'value2')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=value2')
        self.assertEqual(option                 ,   '--option=value2')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value1', args.values[0])


    def test_alias_of_option_with_separate_value(self):

        specifications =   (

            clasp.option('--option', alias = '-o'),
        )
        argv    =   ( 'myprog', '-o', 'value-1', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'value-1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=value-1')
        self.assertEqual(option                 ,   '--option=value-1')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_separate_value(self):

        specifications =   (

            clasp.option('--option', alias = '-o', default_value = 'def-val-1'),
        )
        argv    =   ( 'myprog', '-o', 'value-1', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'value-1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=value-1')
        self.assertEqual(option                 ,   '--option=value-1')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_separate_value_that_resembles_flag(self):

        specifications =   (

            clasp.option('--option', alias = '-o', default_value = 'def-val-1'),
        )
        argv    =   ( 'myprog', '-o', '-o', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   '-o')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=-o')
        self.assertEqual(option                 ,   '--option=-o')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_that_has_default_with_missing_separate_value(self):

        specifications =   (

            clasp.option('--option', alias = '-o', default_value = 'def-val-1'),
        )
        argv    =   ( 'myprog', '-o', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'def-val-1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=def-val-1')
        self.assertEqual(option                 ,   '--option=def-val-1')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_with_attached_empty(self):

        specifications =   (

            clasp.option('--option', alias = '-o', default_value = 'def-val-1'),
        )
        argv    =   ( 'myprog', '-o=', 'value-2', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'def-val-1')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=def-val-1')
        self.assertEqual(option                 ,   '--option=def-val-1')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value-2', args.values[0])


    def test_flag_alias_of_option_with_value(self):

        specifications =   (

            clasp.option('--verbosity'),
            clasp.flag('--verbosity=high', alias = '-v'),
        )
        argv    =   ( 'myprog', '-v', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertFalse(args.flags)
        self.assertEqual(0, len(args.flags))

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   1)
        self.assertEqual(option.given_name      ,   '-v')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'v')
        self.assertEqual(option.name            ,   '--verbosity')
        self.assertEqual(option.value           ,   'high')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--verbosity=high')
        self.assertEqual(option                 ,   '--verbosity=high')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_alias_of_option_with_value(self):

        specifications =   (

            clasp.option('--option', alias = '-o', default_value = 'default-value'),
        )
        argv    =   ( 'myprog', '-f1', 'value-1', '-o=', '-o=given-value-1', '--option=given-value-2', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(1, len(args.flags))


        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-f1')
        self.assertIsNone(flag.argument_specification)
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'f1')
        self.assertEqual(flag.name              ,   '-f1')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '-f1')
        self.assertEqual(flag                   ,   '-f1')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(3, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   3)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'default-value')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=default-value')
        self.assertEqual(option                 ,   '--option=default-value')

        option  =   args.options[1]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   4)
        self.assertEqual(option.given_name      ,   '-o')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   1)
        self.assertEqual(option.given_label     ,   'o')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'default-value')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=default-value')
        self.assertEqual(option                 ,   '--option=default-value')

        option  =   args.options[2]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index     ,   5)
        self.assertEqual(option.given_name      ,   '--option')
        self.assertEqual(option.argument_specification  ,   specifications[0])
        self.assertEqual(option.given_hyphens   ,   2)
        self.assertEqual(option.given_label     ,   'option')
        self.assertEqual(option.name            ,   '--option')
        self.assertEqual(option.value           ,   'default-value')
        self.assertEqual(option.extras          ,   {})
        self.assertEqual(str(option)            ,   '--option=default-value')
        self.assertEqual(option                 ,   '--option=default-value')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertTrue(args.values)
        self.assertEqual(1, len(args.values))

        self.assertEqual('value-1', args.values[0])

    def test_flags_combined(self):

        specifications =   (

            clasp.flag('--compile', alias = '-c'),
            clasp.flag('--debug', alias = '-d'),
            clasp.flag('--execute', alias = '-e'),
        )

        argv    =   ( 'myprog', '-ced', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(3, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-ced')
        self.assertEqual(flag.argument_specification, specifications[0])
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
        self.assertEqual(flag.argument_specification, specifications[2])
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'ced')
        self.assertEqual(flag.name              ,   '--execute')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--execute')
        self.assertEqual(flag                   ,   '--execute')

        flag    =   args.flags[2]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-ced')
        self.assertEqual(flag.argument_specification, specifications[1])
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'ced')
        self.assertEqual(flag.name              ,   '--debug')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--debug')
        self.assertEqual(flag                   ,   '--debug')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertFalse(args.options)
        self.assertEqual(0, len(args.options))

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))


    def test_flags_of_flags_and_options_combined(self):

        specifications =   (

            clasp.flag('--compile', alias = '-c'),
            clasp.flag('--mode=debug', alias = '-d'),
            clasp.flag('--execute', alias = '-e'),
            clasp.option('--mode', alias = '-m'),
        )

        argv    =   ( 'myprog', '-ced', )
        args    =   clasp.parse(argv, specifications)

        self.assertEqual('myprog', args.program_name)

        self.assertIsInstance(args.flags, ( tuple, ))
        self.assertTrue(args.flags)
        self.assertEqual(2, len(args.flags))

        flag    =   args.flags[0]

        self.assertIsInstance(flag, ( Flag, ))
        self.assertEqual(flag.given_index       ,   1)
        self.assertEqual(flag.given_name        ,   '-ced')
        self.assertEqual(flag.argument_specification, specifications[0])
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
        self.assertEqual(flag.argument_specification, specifications[2])
        self.assertEqual(flag.given_hyphens     ,   1)
        self.assertEqual(flag.given_label       ,   'ced')
        self.assertEqual(flag.name              ,   '--execute')
        self.assertEqual(flag.extras            ,   {})
        self.assertEqual(str(flag)              ,   '--execute')
        self.assertEqual(flag                   ,   '--execute')

        self.assertIsInstance(args.options, ( tuple, ))
        self.assertTrue(args.options)
        self.assertEqual(1, len(args.options))

        option  =   args.options[0]

        self.assertIsInstance(option, ( Option, ))
        self.assertEqual(option.given_index       ,   1)
        self.assertEqual(option.given_name        ,   '-ced')
        self.assertEqual(option.argument_specification, specifications[3])
        self.assertEqual(option.given_hyphens     ,   1)
        self.assertEqual(option.given_label       ,   'ced')
        self.assertEqual(option.name              ,   '--mode')
        self.assertEqual(option.extras            ,   {})
        self.assertEqual(str(option)              ,   '--mode=debug')
        self.assertEqual(option                   ,   '--mode=debug')

        self.assertIsInstance(args.values, ( tuple, ))
        self.assertFalse(args.values)
        self.assertEqual(0, len(args.values))



if '__main__' == __name__:

    unittest.main()



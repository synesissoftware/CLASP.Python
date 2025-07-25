#! /usr/bin/env python3

# ######################################################################## #
# File:     tests/test_sections.py
#
# Purpose:  Tests use of sections.
#
# Created:  22nd August 2019
# Updated:  25th July 2025
#
# Copyright (c) Matthew Wilson, Synesis Information Systems Pty Ltd
# All rights reserved
#
# ######################################################################## #


import pyclasp as clasp

import unittest

import sys

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


def _stripped_non_blank_lines_from_SIO(sio):

    s = sio.getvalue().strip()

    lines = s.split("\n")

    lines = [line.strip() for line in lines]

    lines = [line for line in lines if 0 != len(line)]

    return lines


def _stripped_lines_from_SIO(sio):

    s = sio.getvalue().strip()

    lines = s.split("\n")

    lines = [line.strip() for line in lines]

    return lines


class Sections_tester(unittest.TestCase):

    def test_sections_1(self):

        stm     =   StringIO()

        specs   =   (


            clasp.section('Behaviour:'),

            clasp.flag('--verbose', alias='-v', help='Make output verbose'),

            clasp.section('Standard:'),

            clasp.HelpFlag(),
            clasp.VersionFlag(),
        )

        try:
            clasp.show_usage(specs, exit_code=None, stream=stm, info_lines=(), program_name='myprog')

            actual = _stripped_non_blank_lines_from_SIO(stm)

            expected = (

                'USAGE: myprog [ ... flags and options ... ]',
                'flags/options:',
                'Behaviour:',
                '-v',
                '--verbose',
                'Make output verbose',
                'Standard:',
                '--help',
                'Shows usage and terminates',
                '--version',
                'Shows version and terminates',
            )

            self.assertMultiLineEqual(\
                "\n".join(expected),
                "\n".join(actual),
            )

        finally:
            stm.close()


    def test_sections_2(self):

        stm         =   StringIO()

        info_lines  =   (
            "Program suite",
            "Acme Industries",
            ":version:",
            None,
        )

        specs       =   (


            clasp.section('Behaviour:'),

            clasp.flag('--verbose', alias='-v', help='Make output verbose'),

            clasp.section('Standard:'),

            clasp.HelpFlag(),
            clasp.VersionFlag(),
        )

        version     =   '1.2.3'

        try:
            clasp.show_usage(specs, exit_code=None, stream=stm, info_lines=info_lines, program_name='myprog', version=version)

            actual = _stripped_lines_from_SIO(stm)

            expected = (

                "Program suite",
                "Acme Industries",
                "myprog 1.2.3",
                '',
                'USAGE: myprog [ ... flags and options ... ]',
                '',
                'flags/options:',
                '',
                'Behaviour:',
                '',
                '-v',
                '--verbose',
                'Make output verbose',
                '',
                'Standard:',
                '',
                '--help',
                'Shows usage and terminates',
                '',
                '--version',
                'Shows version and terminates',
            )

            self.assertMultiLineEqual(\
                "\n".join(expected),
                "\n".join(actual),
            )

        finally:
            stm.close()


if '__main__' == __name__:

    unittest.main()





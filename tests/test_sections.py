#!/usr/bin/env python

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




if '__main__' == __name__:

    unittest.main()





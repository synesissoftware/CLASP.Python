#!/usr/bin/env python

import pyclasp as clasp

import sys

specifications = (


    clasp.flag('--version', alias = '-v', help = 'show the program version and quits'),

    clasp.option('--verbosity', help = 'the verbosity', values = [ 'silent', 'quiet', 'succinct', 'chatty', 'verbose' ]),
    clasp.option('--length', alias = '-l', help = 'specifies the length'),
    clasp.flag('--verbosity=succinct', aliases = [ '--succinct', '-s' ]),
    clasp.flag('--verbosity=verbose', alias = '--verbose'),
)

info_lines = (

    'CLASP.Python examples',
    ':version',
    "Illustrates use of CLASP.Python's clasp.show_usage() and clasp.show_version() methods",
    '',
)

args = clasp.parse(sys.argv, specifications)

print '*' * 50 + "\n"
print "usage:\n"
clasp.show_usage(args, version = [ 1, 2, 3 ], stream = sys.stdout, program_name = 'myprog', version_prefix = 'v', info_lines = info_lines)

print '*' * 50 + "\n"
print "version:\n"
clasp.show_version(args, version = [ 1, 2, 3 ], stream = sys.stdout, program_name = 'myprog', version_prefix = 'v')

print


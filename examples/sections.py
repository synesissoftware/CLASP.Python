#!/usr/bin/env python

# examples/sections.py


# imports

import pyclasp as clasp

import sys

# constants

VERSION = [ 0, 0, 1 ]

INFO_LINES = (

    'CLASP.Python examples',
    ':version:',
    "Illustrates use of CLASP.Python's clasp.section() to create sections",
    '',
)

# Specify specifications, parse, and checking standard flags

specifications = (

    clasp.section('Behaviour:'),

    clasp.option('--verbosity', alias='-v', help='specifies the verbosity', values=[ 'terse', 'quiet', 'silent', 'chatty' ]),

    clasp.section('Standard:'),

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.parse(sys.argv, specifications)

if args.flag_is_specified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=VERSION, stream=sys.stdout, info_lines=INFO_LINES)

if args.flag_is_specified('--version'):

    clasp.show_version(specifications, exit_code=0, version=VERSION, stream=sys.stdout)


# Program-specific processing of flags/options

opt = args.lookup_option('--verbosity')
if (opt):

    sys.stdout.write("verbosity is specified as: %s\n" % opt.value)


# Check for any unrecognised flags or options

unused = args.get_first_unused_flag_or_option();
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)


sys.stdout.write("no flags specified\n");



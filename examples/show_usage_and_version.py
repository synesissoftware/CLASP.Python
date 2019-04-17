#!/usr/bin/env python

# examples/show_usage_and_version.py


# imports

import pyclasp as clasp

import sys

# constants

version = [ 0, 0, 1 ]

info_lines = (

    'CLASP.Python examples',
    ':version:',
    "Illustrates use of CLASP.Python's clasp.show_usage() and clasp.show_version() methods",
    '',
)

# Specify specifications, parse, and checking standard flags

specifications = (

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.parse(sys.argv, specifications)

if args.flagIsSpecified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=version, stream=sys.stdout, info_lines = info_lines)

if args.flagIsSpecified('--version'):

    clasp.show_version(specifications, exit_code=0, version=version, stream=sys.stdout)


# Check for any unrecognised flags or options

unused = args.getFirstUnusedFlagOrOption();
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)


sys.stdout.write("no flags specified\n");


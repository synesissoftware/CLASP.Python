#!/usr/bin/env python

# examples/flags_and_options_specifications.py


# imports

import pyclasp as clasp

import sys

# constants

version = [ 0, 0, 1 ]

info_lines = (

    'CLASP.Python examples',
    ':version:',
    "Illustrates use of CLASP.Python's use of flags, options, and specifications",
    '',
)

# Specify specifications, parse, and checking standard flags

flag_Debug = clasp.flag('--debug', alias='-d', help='runs in Debug mode');
option_Verbosity = clasp.option('--verbosity', alias='-v', help='specifies the verbosity', values=[ 'terse', 'quiet', 'silent', 'chatty' ]);
flag_Chatty = clasp.flag('--verbosity=chatty', alias='-c');

specifications = (

    flag_Debug,
    option_Verbosity,
    flag_Chatty,

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.parse(sys.argv, specifications)

if args.flagIsSpecified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=version, stream=sys.stdout, info_lines = info_lines)

if args.flagIsSpecified('--version'):

    clasp.show_version(specifications, exit_code=0, version=version, stream=sys.stdout)


# Program-specific processing of flags/options

opt = args.lookupOption('--verbosity')
if (opt):

    sys.stdout.write("verbosity is specified as: %s\n" % opt.value)


if (args.flagIsSpecified('--debug')):

    sys.stdout.write("Debug mode is specified\n")


# Check for any unrecognised flags or options

unused = args.getFirstUnusedFlagOrOption();
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)



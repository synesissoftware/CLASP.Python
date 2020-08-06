#! /usr/bin/env python

# examples/multiple_options.py


# imports

import pyclasp as clasp

import sys

# constants

VERSION = [ 0, 0, 1 ]

INFO_LINES = (

    'CLASP.Python examples',
    ':version:',
    "Illustrates use of CLASP.Python's support for multiple specification of options",
    '',
)

# Specify specifications, parse, and checking standard flags

option_Extension = clasp.option('--extension', alias='-e', help='specifies a file extension. May be specified multiple times', on_multiple='allow')
flag_CalcDirSize = clasp.flag('--calc-dir-size', alias='-z', help='causes directory sizes to be calculated')

specifications = (

    option_Extension,
    flag_CalcDirSize,

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.parse(sys.argv, specifications)

if args.flag_is_specified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=VERSION, stream=sys.stdout, info_lines=INFO_LINES)

if args.flag_is_specified('--version'):

    clasp.show_version(specifications, exit_code=0, version=VERSION, stream=sys.stdout)


# List all flags and options for your edification

for f in args.flags:

    print("flag: %s" % f)

    f.use()

for o in args.options:

    print("option: %s" % o)

    o.use()



# Check for any unrecognised flags or options

unused = args.get_first_unused_flag_or_option()
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)



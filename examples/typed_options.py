#!/usr/bin/env python

import pyclasp as clasp

import sys

# constants

version = '0.0.1'

info_lines = (

    'CLASP.Python examples',
    ':version',
    "Illustrates use of CLASP.Python's typed option values",
    '',
)

# Specify specifications, parse, and checking standard flags

specifications = (

    clasp.HelpFlag(),
    clasp.VersionFlag(),

    clasp.option('--length', alias = '-l', help = 'specifies the length', value_type=int),
)

try:

    args = clasp.parse(sys.argv, specifications)
except clasp.ValueParsingException as x:

    sys.stderr.write("%s: invalid command line: %s\n" % (clasp.get_program_name(), x))

    sys.exit(1)


if args.flagIsSpecified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=version, stream=sys.stdout, info_lines = info_lines)

if args.flagIsSpecified('--version'):

    clasp.show_version(specifications, exit_code=0, version=version, stream=sys.stdout)


# Program-specific processing of flags/options

opt_length = args.lookup_option('--length')
if opt_length:

    print("You specified length with the value: %d (of type %s). The string that was passed is available in the 'given_value' attribute, which is '%s' (of type %s)\n" % (opt_length.value, type(opt_length.value), opt_length.given_value, type(opt_length.given_value)))
else:

    sys.stderr.write("try specifying the '--length' option; use --help for usage\n")

    sys.exit(1)



# Check for any unrecognised flags or options

unused = args.getFirstUnusedFlagOrOption();
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)



#! /usr/bin/env python

# examples/duplicate_aliases.py


# imports

import pyclasp as clasp

import sys

# Specify specifications, parse, and checking standard flags

flag_Compile    =   clasp.flag('--compile', alias='-c')
flag_Debug      =   clasp.flag('--debug', alias='-d')
flag_Execute    =   clasp.flag('--execute', alias='-c')

specifications = (

    flag_Compile,
    flag_Debug,
    flag_Execute,

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.parse(sys.argv, specifications)


if args.flag_is_specified('--help'):

    clasp.show_usage(specifications, exit_code=0, stream=sys.stdout)
else:

    sys.stderr.write("specify the '--help' flag to observe the duplicate alias warning\n")



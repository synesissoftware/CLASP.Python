# CLASP.Python Example - **duplicate_aliases**

## Summary

Example illustrating how the library will warn about duplicate aliases

## Source

```python
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
```

## Usage

If executed with the arguments

```
$ python examples/multiple_options.py --help
```

it gives the following output on the standard output stream:

```
USAGE: duplicate_aliases.py [ ... flags and options ... ]

flags/options:

	-c
	--compile
		None

	-d
	--debug
		None

	-c
	--execute
		None

	--help
		Shows usage and terminates

	--version
		Shows version and terminates
```

and it gives the following output on the standard error stream:

```
WARNING: alias '-c' is already used for specification '<pyclasp.flag_specification.FlagSpecification: name=--execute; help=None; aliases=('-c',); extras={}>'
```



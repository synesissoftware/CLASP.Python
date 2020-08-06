# CLASP.Python Example - **flag_and_option_specifications**

## Summary

Example illustrating various kinds of *flag* and *option* specifications, including the combination of short-names.

## Source

```python
#!/usr/bin/env python

# examples/flags_and_options_specifications.py


# imports

import pyclasp as clasp

import sys

# constants

VERSION = [ 0, 0, 2 ]

INFO_LINES = (

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

if args.flag_is_specified('--help'):

    clasp.show_usage(specifications, exit_code=0, version=VERSION, stream=sys.stdout, info_lines=INFO_LINES)

if args.flag_is_specified('--version'):

    clasp.show_version(specifications, exit_code=0, version=VERSION, stream=sys.stdout)


# Program-specific processing of flags/options

opt = args.lookup_option('--verbosity')
if (opt):

    sys.stdout.write("verbosity is specified as: %s\n" % opt.value)


if (args.flag_is_specified('--debug')):

    sys.stdout.write("Debug mode is specified\n")


# Check for any unrecognised flags or options

unused = args.get_first_unused_flag_or_option();
if (unused):

    sys.stderr.write("%s: unrecognised flag/option: %s\n" % (args.program_name, unused))

    sys.exit(1)
```

## Usage

### No arguments

If executed with no arguments

```
    python examples/flag_and_option_specifications.py
```

or (in a Unix shell):

```
    ./examples/flag_and_option_specifications.py
```

it gives the output:

```
```

### Show usage

If executed with the arguments

```
    python examples/flag_and_option_specifications.py --help
```

it gives the output:

```
CLASP.Python examples
flag_and_option_specifications.py 0.0.2
Illustrates use of CLASP.Python's use of flags, options, and specifications

USAGE: flag_and_option_specifications.py [ ... flags and options ... ]

flags/options:

	-d
	--debug
		runs in Debug mode

	-c --verbosity=chatty
	-v <value>
	--verbosity=<value>
		specifies the verbosity
		where <value> one of:
			terse
			quiet
			silent
			chatty

	--help
		Shows usage and terminates

	--version
		Shows version and terminates
```

### Specify flags and options in long-form

If executed with the arguments

```
    python examples/flag_and_option_specifications.py --debug --verbosity=silent
```

it gives the output:

```
verbosity is specified as: silent
Debug mode is specified
```

### Specify flags and options in short-form

If executed with the arguments

```
    python examples/flag_and_option_specifications.py -v silent -d
```

it gives the (same) output:

```
verbosity is specified as: silent
Debug mode is specified
```

### Specify flags and options in short-form, including an alias for an option-with-value

If executed with the arguments

```
    python examples/flag_and_option_specifications.py -c -d
```

it gives the output:

```
verbosity is specified as: chatty
Debug mode is specified
```

### Specify flags and options with combined short-form

If executed with the arguments

```
    python examples/flag_and_option_specifications.py -dc
```

it gives the (same) output:

```
verbosity is specified as: chatty
Debug mode is specified
```


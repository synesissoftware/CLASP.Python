# CLASP.Python Example - **show_usage_and_version**

## Summary

Example illustrating various kinds of *flag* and *option* aliases, including the combination of short-names.

## Source

```python
#!/usr/bin/env python

# examples/flags_and_options_aliases.py


# imports

import pyclasp as clasp

import sys

# constants

version = [ 0, 0, 1 ]

info_lines = (

    'CLASP.Python examples',
    ':version:',
    "Illustrates use of CLASP.Python's use of flags, options, and aliases",
    '',
)

# Specify aliases, parse, and checking standard flags

flag_Debug = clasp.flag('--debug', alias='-d', help='runs in Debug mode');
option_Verbosity = clasp.option('--verbosity', alias='-v', help='specifies the verbosity', values=[ 'terse', 'quiet', 'silent', 'chatty' ]);
flag_Chatty = clasp.flag('--verbosity=chatty', alias='-c');

aliases = (

    flag_Debug,
    option_Verbosity,
    flag_Chatty,

    clasp.HelpFlag(),
    clasp.VersionFlag(),
)

args = clasp.Arguments(sys.argv, aliases)

if args.flagIsSpecified('--help'):

    clasp.show_usage(aliases, exit_code=0, version=version, stream=sys.stdout, info_lines = info_lines)

if args.flagIsSpecified('--version'):

    clasp.show_version(aliases, exit_code=0, version=version, stream=sys.stdout)


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
```

## Usage

### No arguments

If executed with no arguments

```
    python examples/flag_and_option_aliases.py
```

or (in a Unix shell):

```
    ./examples/flag_and_option_aliases.py
```

it gives the output:

```
```

### Show usage

If executed with the arguments

```
    python examples/flag_and_option_aliases.py --help
```

it gives the output:

```
CLASP.Python examples
flag_and_option_aliases.py 0.0.1
Illustrates use of CLASP.Python's use of flags, options, and aliases

USAGE: flag_and_option_aliases.py [ ... flags and options ... ]

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
    python examples/flag_and_option_aliases.py --debug --verbosity=silent
```

it gives the output:

```
verbosity is specified as: silent
Debug mode is specified
```

### Specify flags and options in short-form

If executed with the arguments

```
    python examples/flag_and_option_aliases.py -v silent -d
```

it gives the (same) output:

```
verbosity is specified as: silent
Debug mode is specified
```

### Specify flags and options in short-form, including an alias for an option-with-value

If executed with the arguments

```
    python examples/flag_and_option_aliases.py -c -d
```

it gives the output:

```
verbosity is specified as: chatty
Debug mode is specified
```

### Specify flags and options with combined short-form

If executed with the arguments

```
    python examples/flag_and_option_aliases.py -dc
```

it gives the (same) output:

```
verbosity is specified as: chatty
Debug mode is specified
```


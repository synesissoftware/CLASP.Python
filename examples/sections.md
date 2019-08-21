# CLASP.Python Example - **sections**

## Summary

Simple example supporting ```--help``` and ```--version```.

## Source

```python
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
```

## Usage

### No arguments

If executed with no arguments

```
    python examples/sections.py
```

or (in a Unix shell):

```
    ./examples/sections.py
```

it gives the output:

```
no flags specified
```

### Show usage

If executed with the arguments

```
    python examples/sections.py --help
```

it gives the output:

```
CLASP.Python examples
sections.py 0.0.1
Illustrates use of CLASP.Python's clasp.section() to create sections

USAGE: sections.py [ ... flags and options ... ]

flags/options:

	Behaviour:

	-v <value>
	--verbosity=<value>
		specifies the verbosity
		where <value> one of:
			terse
			quiet
			silent
			chatty

	Standard:

	--help
		Shows usage and terminates

	--version
		Shows version and terminates
```

### Show version

If executed with the arguments

```
    python examples/sections.py --version
```

it gives the output:

```
sections.py 0.0.1
```

### Unknown option

If executed with the arguments

```
    python examples/sections.py --unknown=value
```

it gives the output (on the standard error stream):

```
sections.py: unrecognised flag/option: --unknown=value
```

with an exit code of 1



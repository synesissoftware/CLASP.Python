# CLASP.Python Example - **typed_options**

## Summary

Simple example supporting ```--help``` and ```--version```.

## Source

```python
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
```

## Usage

### No arguments

If executed with no arguments

```
    python examples/typed_options.py
```

or (in a Unix shell):

```
    ./examples/typed_options.py
```

it gives the output:

```
try specifying the '--length' option; use --help for usage
```

### Show usage

If executed with the arguments

```
    python examples/typed_options.py --help
```

it gives the output:

```
CLASP.Python examples
typed_options.py 0.0.1
Illustrates use of CLASP.Python's typed option values

USAGE: typed_options.py [ ... flags and options ... ]

flags/options:

	--help
		Shows usage and terminates

	--version
		Shows version and terminates

	-l <value>
	--length=<value>
		specifies the length
```

### Specify a valid length

If executed with the arguments

```
    python examples/typed_options.py --length=10
```

it gives the output:

```
You specified length with the value: 10 (of type <type 'int'>). The string that was passed is available in the 'given_value' attribute, which is '10' (of type <type 'str'>)
```

### Specify a missing length

If executed with the arguments

```
    python examples/typed_options.py --length=
```

it gives the output (on the standard error stream):

```
typed_options.py: invalid command line: the '--length' option does not have a value to be interpreted as an integer
```

with an exit code of 1

### Specify an invalid length

If executed with the arguments

```
    python examples/typed_options.py --length=abc
```

it gives the output (on the standard error stream):

```
typed_options.py: invalid command line: the '--length' option's value 'abc' cannot be interpreted as an integer
```

with an exit code of 1


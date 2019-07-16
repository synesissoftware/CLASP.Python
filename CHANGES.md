# **CLASP.Python** Changes

## 0.5.2 - 16th July 2019

* ~ fixed ``lookup_flag()``/``lookup_option()`` such that can now be passed specifications as well as strings for id
* ~ compatibility for StringIO for Python 2/3

## 0.5.1 - 12th June 2019

* ~ improving flexibility of handling of options to ``show_usage()``

## 0.5.0 - 25th April 2019

* + added ``OptionArgument.given_value`` attribute, which is always the string that is given during parsing
* + now supports 'value_type' named parameter in option specifications, whose value can be ``None`` (default), ``float``, or ``int``. For ``float`` and ``int`` a successful parse of the option value means that the ``OptionArgument.value`` attribute will be a ``float`` or ``int`` converted from the given value

## 0.4.2 - 25th April 2019

* ~ ensuring that all flag/option arguments receive the correct (underlying) flag/option specifications

## 0.4.1 - 25th April 2019

* ~ fixed type in exception message in ``option()``

## 0.4.0 - 17th April 2019

* ~ changed *Alias classes to *Specification
* ~ clasp.Arguments aliases attribute is now changed to specifications, and a [DEPRECATED] #aliases added

## 0.3.1 - 17th April 2019

* ~ fixed defect whereby sys.argv[0] was not used correctly to determine program name
* ~ show_usage() and show_version() now handle case whereby first argument is instance of clasp.Arguments, as well as aliases
* ~ moved around some internal methods to simplify intra-library dependencies
* ~ ensured internal methods named with leading underscore


## previous versions

T.B.C.



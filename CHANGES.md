# **CLASP.Python** Changes

## 0.8.8 - 24th August 2020

* ~ fixing defect in option default value processing

## 0.8.7 - 24th August 2020

* ~ fixing defect in option value processing

## 0.8.6 - 17th August 2020

* ~ ``show_usage()`` now issues a warning message to stderr for duplicate aliases (consistent with behaviour of (CLASP.Ruby)[https://github.com/synesissoftware/CLASP.Ruby])

## 0.8.5 - 13th August 2020

* ~ fixing compatibility with Python 3's removal of ``long``

## 0.8.4 - 12th August 2020

* allows ``OptionSpecification``'s ``value_type`` to be ``bool``
* added ``InvalidBooleanException`` exception class

## 0.8.3 - 12th August 2020

* allows ``OptionSpecification``'s ``value_type`` to be ``long``

## 0.8.2 - 12th August 2020

* allows ``OptionSpecification``'s ``value_type`` to be ``str``

## 0.8.1 - 11th August 2020

* can now compare equal ``Flag`` instances with ``FlagSpecification`` instances and ``Option`` instances with ``OptionSpecification`` instances
* significantly expanded unit-tests

## 0.8.0 - 6th August 2020

* added ``on_multiple`` keyword argument to ``OptionSpecification``
* added ``DuplicateFlagSpecified`` exception class
* added ``DuplicateOptionSpecified`` exception class
* added ``ParsingException`` exception class
* added examples/multiple_options.py (and examples/multiple_options.md)

## 0.7.1 - 4th August 2020

* ~ various tidyings

## 0.7.0 - 22nd August 2019

* + added sections, via ``clasp.section()``
* + added examples/sections.py (and examples/section.md)

## 0.6.1 - 22nd August 2019

* ~ fixed defect in ``get_first_unused_flag_or_option()`` introduced in 0.6.0

## 0.6.0 - 19th August 2019

* ~ ``get_first_unused_flag()``, ``get_first_unused_option()``, ``get_first_unused_flag_or_option()`` all now take an optional ``id`` parameter, which may be a flag/option or a string, that constrains the search

## 0.5.3 - 16th July 2019

* ~ increased flexibility of dealing with ``flags_and_options`` and ``values_string``

## 0.5.2 - 16th July 2019

* ~ fixed ``lookup_flag()``/``lookup_option()`` such that can now be passed specifications as well as strings for id
* ~ compatibility for StringIO for Python 2/3
* ~ updated examples to use non-deprecated constructs

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




__author__      =   "Matt Wilson"
__copyright__   =   "Copyright 2019-2026 Synesis Information Systems, Copyright 2019 Synesis Software"
__credits__     =   [

        "Garth Lancaster",
        "Matt Wilson",
 ]
__email__       =   "matthew@synesis.com.au"
__license__     =   "BSD-3-Clause"
__maintainer__  =   "Matt Wilson"
__status__      =   "Beta"
__version__     =   "0.8.13"

from .exceptions import (
	CLASPException as CLASPException,
	DuplicateFlagSpecified as DuplicateFlagSpecified,
	DuplicateOptionSpecified as DuplicateOptionSpecified,
	IntegerOutOfRangeException as IntegerOutOfRangeException,
	InvalidBooleanException as InvalidBooleanException,
	InvalidIntegerException as InvalidIntegerException,
	InvalidNumberException as InvalidNumberException,
	InvalidValueException as InvalidValueException,
	MissingValueException as MissingValueException,
	ParsingException as ParsingException,
	ValueParsingException as ValueParsingException,
)
from .flag_specification import FlagSpecification as FlagSpecification
from .flag_specification import HelpFlag as HelpFlag
from .flag_specification import VersionFlag as VersionFlag
from .flag_specification import flag as flag
from .option_specification import OptionSpecification as OptionSpecification
from .option_specification import option as option
from .section_specification import SectionSpecification as SectionSpecification
from .section_specification import section as section
from .specification import Specification as Specification
from .specification import specification as specification

from .arguments import Arguments
from .flag_argument import FlagArgument as Flag  # noqa: F401
from .option_argument import OptionArgument as Option  # noqa: F401

from .cli import show_usage as show_usage
from .cli import show_version as show_version

import sys

def parse(argv = None, specifications = None):
    """
    Obtains an instance of `clasp.Arguments`, representing all the command-line arguments present in `argv` (or `sys.argv`)
    """

    if argv is None:

        argv = sys.argv

    return Arguments(argv, specifications)

def get_program_name(argv = None):
    """
    Obtains/infers the program name from the given array, or from `sys.argv`
    """

    return Arguments.get_program_name(argv)


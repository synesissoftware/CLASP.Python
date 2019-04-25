
__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2019, Synesis Software'
__credits__     =   [
        'Garth Lancaster',
        'Matt Wilson',
 ]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Beta'
__version__     =   '0.4.2'

from .flag_specification import FlagSpecification, flag
from .flag_specification import HelpFlag, VersionFlag
from .option_specification import OptionSpecification, option
from .specification import Specification, specification

from .arguments import Arguments
from .flag_argument import FlagArgument as Flag
from .option_argument import OptionArgument as Option

from .cli import show_usage, show_version

import sys

def parse(argv = None, specifications = None):

    argv    =   argv if None != type(argv) else sys.argv

    return Arguments(argv, specifications)



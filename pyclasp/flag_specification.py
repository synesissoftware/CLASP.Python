
from .specification import Specification

class FlagSpecification(Specification):

    def __init__(self, name, aliases, help, extras):

        super(FlagSpecification, self).__init__(name, aliases, help, extras)

    def __str__(self):

        return "<%s.%s: name=%s; help=%s; aliases=%s; extras=%s>" %\
            (self.__module__, self.__class__.__name__, self.name, self.help, self.aliases, self.extras)


def flag(name, **kwargs):
    """Creates a flag specification from the given parameters"""

    aliases =   None
    help    =   None
    extras  =   None

    for n, v in kwargs.items():

        if 'alias' == n:

            aliases = ( v, )
        elif 'aliases' == n:

            aliases = v
        elif 'help' == n:

            help = v
        elif 'extras' == n:

            extras = v
        else:

            raise TypeError("'flag' method does not recognise the '%s' keyword argument" % (n, ))

    return FlagSpecification(name, aliases, help, extras)

_HELP_FLAG      =   FlagSpecification('--help', None, 'Shows usage and terminates', None)
_VERSION_FLAG   =   FlagSpecification('--version', None, 'Shows version and terminates', None)


def HelpFlag():

   return _HELP_FLAG

def VersionFlag():

   return _VERSION_FLAG



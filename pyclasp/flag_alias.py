
from .alias import Alias

class FlagAlias(Alias):

    def __init__(self, name, aliases, help, extras):

        super(FlagAlias, self).__init__(name, aliases, help, extras)

    def __str__(self):

        return "<%s.%s: name=%s; help=%s; aliases=%s; extras=%s>" %\
            (self.__module__, self.__class__.__name__, self.name, self.help, self.aliases, self.extras)


def flag(name, **kwargs):

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

    return FlagAlias(name, aliases, help, extras)

HELP_FLAG_      =   FlagAlias('--help', None, 'Shows usage and terminates', None)
VERSION_FLAG_   =   FlagAlias('--version', None, 'Shows version and terminates', None)


def HelpFlag():

   return HELP_FLAG_

def VersionFlag():

   return VERSION_FLAG_




from .alias import Alias

class FlagAlias(Alias):

    def __init__(self, name, aliases, help, extras):

        super(FlagAlias, self).__init__(name, aliases, help, extras)


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



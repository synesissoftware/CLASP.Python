
class Specification(object):

    def __init__(self, name, aliases, help, extras):

        if not isinstance(name, str):

            raise TypeError("'name' must be of type 'str'")


        if aliases:

            if not isinstance(aliases, ( list, tuple )):

                raise TypeError("'aliases' must be None or an instance of 'list' or 'tuple'")
        else:

            aliases = ()


        if help:

            if not isinstance(help, ( str, )):

                raise TypeError("'help' must be an instance of 'str'")


        if extras:

            if not isinstance(extras, ( dict, )):

                raise TypeError("'extras must be None or an instance of 'dict'")

        else:

            extras  =   {}


        self.name       =   name
        self.aliases    =   aliases
        self.help       =   help
        self.extras     =   extras


def specification(name, **kwargs):

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

            raise TypeError("'specification' method does not recognise the '%s' keyword argument" % (n, ))

    return Specification(name, aliases, help, extras)



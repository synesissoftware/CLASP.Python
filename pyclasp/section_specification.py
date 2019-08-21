
from .specification import Specification

class SectionSpecification(Specification):

    def __init__(self, name, extras):

        super(SectionSpecification, self).__init__(name, None, None, extras)

    def __str__(self):

        return "<%s.%s: name=%s; help=%s; aliases=%s; extras=%s>" %\
            (self.__module__, self.__class__.__name__, self.name, self.help, self.aliases, self.extras)


def section(name, **kwargs):
    """Creates a section specification from the given parameters"""

    extras  =   None

    for n, v in kwargs.items():

        if False:

            pass
        elif 'extras' == n:

            extras = v
        else:

            raise TypeError("'section' method does not recognise the '%s' keyword argument" % (n, ))

    return SectionSpecification(name, extras)




import sys

class FlagArgument:

    def __init__(self, arg, given_index, given_name, resolved_name, argument_alias, given_hyphens, given_label, extras):

        self.arg_           =   arg
        self.given_index    =   given_index
        self.given_name     =   given_name
        self.argument_alias =   argument_alias
        self.given_hyphens  =   given_hyphens
        self.given_label    =   given_label
        self.name           =   resolved_name if resolved_name else given_name
        self.extras         =   extras if extras else dict()

        self.private_fields =   {

            'used'  :   False
        }

    def use(self):

        self.private_fields['used'] = True

    def used(self):

        return self.private_fields['used']

    def __str__(self):

        #sys.stderr.write("__str__(self=%s)\n" % (self.name))

        return self.name

    def __eq__(self, other):
        """Yields True if other is a FlagArgument and has the same 'name'"""

        #sys.stderr.write("__eq__(self=%s, other=%s)\n" % (self, other))

        if isinstance(other, FlagArgument):

            return self.name == other.name

        if isinstance(other, str):

            return self.name == other

        return False


    def __ne__(self, other):
        """Yields False if other is not a FlagArgument or has a different 'name'"""

        #sys.stderr.write("__ne__(self=%s, other=%s)\n" % (self, other))

        return not self.__eq__(other)



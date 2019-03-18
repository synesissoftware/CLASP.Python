
import sys

class OptionArgument(object):

    def __init__(self, arg, given_index, given_name, resolved_name, argument_alias, given_hyphens, given_label, value, extras):

        self.arg_           =   arg
        self.given_index    =   given_index
        self.given_name     =   given_name
        self.argument_alias =   argument_alias
        self.given_hyphens  =   given_hyphens
        self.given_label    =   given_label
        self.name           =   resolved_name if resolved_name else given_name
        self.value          =   value
        self.extras         =   extras if extras else dict()

        self.private_fields =   {

            'used'  :   False
        }

    def use(self):

        self.private_fields['used'] = True

    def used(self):

        return self.private_fields['used']

    def __str__(self):

        return "%s=%s" % (self.name, self.value)

    def __eq__(self, other):
        """Yields True if other is a OptionArgument and has the same 'name'"""

        if isinstance(other, OptionArgument):

            return str(self) == str(other)

        if isinstance(other, str):

            return str(self) == other

        return False


    def __ne__(self, other):
        """Yields False if other is not a OptionArgument or has a different 'name'"""

        sys.stderr.write("__ne__(self=%s, other=%s)\n" % (self, other))

        return not self.__eq__(other)



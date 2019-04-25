
from .option_specification import OptionSpecification

class OptionArgument(object):

    def __init__(self, arg, given_index, given_name, resolved_name, argument_specification, given_hyphens, given_label, value, extras):

        if __debug__:
            if not argument_specification:

                pass
            elif isinstance(argument_specification, (OptionSpecification, )):

                pass
            else:

                raise TypeError("'argument_specification' must be instance of type '%s'; '%s' (%s) given" % (OptionSpecification, type(argument_specification), argument_specification))

        self.arg_           =   arg
        self.given_index    =   given_index
        self.given_name     =   given_name
        self.argument_specification =   argument_specification
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

        return not self.__eq__(other)



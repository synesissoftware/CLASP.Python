
from .exceptions import *
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
        self._set_value(value, True)
        self.extras         =   extras if extras else dict()

        self.private_fields =   {

            'used'  :   False
        }

    def _set_value(self, value, from_ctor=False):

        given_value         =   value

        arg_spec            =   self.argument_specification

        if arg_spec:

            if not given_value:

                given_value = arg_spec.default_value

            if given_value:


                if arg_spec.value_type:

                    assert arg_spec.value_type in OptionSpecification._VALID_VALUE_TYPES

                    if False:

                        pass
                    elif arg_spec.value_type == float:

                        try:

                            value       =   float(given_value)
                        except ValueError as x:

                            raise InvalidNumberException("the '%s' option's value '%s' cannot be interpreted as a number" % (self.name, given_value))
                    elif arg_spec.value_type == int:

                        try:

                            value       =   int(given_value)
                        except ValueError as x:

                            raise InvalidIntegerException("the '%s' option's value '%s' cannot be interpreted as an integer" % (self.name, given_value))


            else:

                if given_value is None and from_ctor:

                    pass
                else:

                    raise MissingValueException("the '%s' option does not have a value to be interpreted as an integer" % (self.name))


        self.given_value    =   given_value
        self.value          =   value


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



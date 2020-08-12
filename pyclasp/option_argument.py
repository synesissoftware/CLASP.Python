
from .exceptions import *
from .option_specification import OptionSpecification

_FALSE_STRINGS_lower = (

    "false",
    "no",
    "0",
)
_TRUE_STRINGS_lower = (

    "true",
    "yes",
    "1",
)

def _parse_to_bool(v):

    s   =   str(v)

    s   =   s.lower()

    if s in _FALSE_STRINGS_lower:

        return False

    if s in _TRUE_STRINGS_lower:

        return True

    return None

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
                    elif arg_spec.value_type == bool:

                        try:

                            value       =   _parse_to_bool(given_value)
                        except ValueError as x:

                            raise InvalidBooleanException("the '%s' option's value '%s' cannot be interpreted as boolean" % (self.name, given_value))
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
                    elif arg_spec.value_type == long:

                        try:

                            value       =   long(given_value)
                        except ValueError as x:

                            raise InvalidIntegerException("the '%s' option's value '%s' cannot be interpreted as a long integer" % (self.name, given_value))
                    elif arg_spec.value_type == str:

                        value   =   given_value
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

        if isinstance(self.value, (bool, )):

            v   =   str(self.value).lower()
        else:

            v   =   str(self.value)

        return "%s=%s" % (self.name, v)

    def __repr__(self):

        return "<%s.%s: given_index=%s; given_name=%s; given_value=%s; given_hyphens=%s, given_label=%s, extras=%s; argument_specification=%s >" %\
            (self.__module__, self.__class__.__name__, self.given_index, self.given_name, self.given_value, self.given_hyphens, self.given_label, self.extras, self.argument_specification, )

    def __eq__(self, other):
        """Yields True if other is a string that is the same as 'name', or a OptionArgument or a OptionSpecification that has the same 'name'"""

        if isinstance(other, OptionArgument):

            return str(self) == str(other)

        if isinstance(other, OptionSpecification):

            return self.name == other.name

        if isinstance(other, str):

            return str(self) == other

        return False

    def __ne__(self, other):
        """Yields False if other is not a OptionArgument or has a different 'name'"""

        return not self.__eq__(other)



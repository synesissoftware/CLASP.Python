
from .specification import Specification
from .util import _MULTIPLE_OPTION_ACTION_DEFAULT, _MULTIPLE_ACTION_OPTION_ALLOWED

class OptionSpecification(Specification):

    _VALID_VALUE_TYPES = (float, int, long, str, )

    def __init__(self, name, aliases, help, extras, values_range, default_value, is_required, require_message, value_type, on_multiple):

        super(OptionSpecification, self).__init__(name, aliases, help, extras)

        self.values_range       =   values_range
        self.default_value      =   default_value
        self.is_required        =   is_required
        self.require_message    =   require_message
        self.value_type         =   value_type
        self.on_multiple        =   on_multiple

    def __str__(self):

        return "<%s.%s: name=%s; help=%s; aliases=%s; extras=%s, default_value=%s, values_range=%s, on_multiple=%s, is_required=%s, require_message=%s >" %\
            (self.__module__, self.__class__.__name__, self.name, self.help, self.aliases, self.extras, self.default_value, self.values_range, self.on_multiple, self.is_required, self.require_message,)


def option(name, **kwargs):
    """Creates an option specification from the given parameters"""

    aliases =   None
    help    =   None
    extras  =   None

    values_range    =   None
    default_value   =   None
    is_required     =   None
    require_message =   None
    value_type      =   None
    on_multiple     =   _MULTIPLE_OPTION_ACTION_DEFAULT

    for n, v in kwargs.items():

        if False:

            pass
        elif 'alias' == n:

            aliases = ( v, )
        elif 'aliases' == n:

            aliases = v
        elif 'help' == n:

            help = v
        elif 'extras' == n:

            extras = v
        elif 'values_range' == n or 'values' == n:

            values_range = v
        elif 'default_value' == n or 'default' == n:

            default_value = v
        elif 'required' == n or 'is_required' == n:

            is_required = v
        elif 'on_multiple' == n:

            if v is None:

                pass
            elif str == type(v):

                v = v.upper()

                if v not in _MULTIPLE_ACTION_OPTION_ALLOWED:

                    raise TypeError("'option' method keyword argument 'on_multiple' must be one of %s (in any case); '%s' given" % (_MULTIPLE_ACTION_OPTION_ALLOWED, v))

            else:

                raise TypeError("'option' method keyword argument 'on_multiple' must be 'None' or a string; '%s' (%s) given" % (v, type(v)))

            on_multiple = v
        elif 'require_message' == n:

            require_message = v
        elif 'value_type' == n:

            value_type = v

            if value_type is None:

                pass
            elif value_type in OptionSpecification._VALID_VALUE_TYPES:

                pass
            else:

                raise TypeError("'option' method supports 'value_type' but only for 'None', 'float', 'int', 'long', and 'str'; '%s' (%s) given" % (value_type, type(value_type)))
        else:

            raise TypeError("'option' method does not recognise the '%s' keyword argument" % (n, ))

    return OptionSpecification(name, aliases, help, extras, values_range, default_value, is_required, require_message, value_type, on_multiple)



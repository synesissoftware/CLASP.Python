
class CLASPException(RuntimeError):
    """Root exception for CLASP"""

    pass

class ParsingException(CLASPException):
    """Root exception for parsing"""

    pass

class ValueParsingException(ParsingException):
    """Root exception for value parsing"""

    pass

class MissingValueException(ValueParsingException):
    """Used to indicate that no value is specified for an option (and its specification, if any, does not have a default)"""

    pass

class InvalidValueException(ValueParsingException):
    """Root exception for invalid values"""

    pass

class InvalidNumberException(InvalidValueException):
    """The given value could not be recognised as a (properly-formatted) number"""

    pass

class InvalidIntegerException(InvalidNumberException):
    """The given value could not be recognised as a (properly-formatted) integer"""

    pass

class IntegerOutOfRangeException(InvalidValueException):
    """The given value as a valid integer but is out of range"""

    pass

class DuplicateFlagSpecified(ParsingException):
    """Used to indicate that a duplicate flag is specified"""

    def __init__(self, existing, current, spec):

        self.existing   =   existing
        """The existing flag that is duplicated"""

        self.current    =   current
        """The new flag that is a duplicate"""

        self.specification  =   spec
        """The specification of the flag, if any"""

class DuplicateOptionSpecified(ParsingException):
    """Used to indicate that a duplicate option is specified"""

    def __init__(self, existing, current, spec):

        self.existing   =   existing
        """The existing option that is duplicated"""

        self.current    =   current
        """The new option that is a duplicate"""

        self.specification  =   spec
        """The specification of the option, if any"""


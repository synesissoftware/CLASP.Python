
class CLASPException(RuntimeError):
    """Root exception for CLASP"""

    pass

class ValueParsingException(CLASPException):
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


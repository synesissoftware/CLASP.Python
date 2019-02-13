
from .flag import Flag
from .option import Option

import re

class Arguments:

    def __init__(self, argv, aliases = None):

        if not isinstance(argv, ( list, tuple )):

            raise TypeError("argv argument must be a 'list' or a 'tuple'")


        self.argv       =   argv

        self.aliases    =   aliases

        flags, options, values  =   Arguments._parse(argv, aliases)

        for arg in argv:

            pass

        self.flags      =   tuple(flags)
        """The parsed flags"""

        self.options    =   tuple(options)
        """The parsed options"""

        self.values     =   tuple(values)
        """The parsed values"""


    @staticmethod
    def _parse(argv, aliases):

        flags           =   []
        options         =   []
        values          =   []

        forced_value    =   False
        want_opt_value  =   False

        for index, arg in enumerate(argv):

            if not forced_value:

                if '--' == arg:

                    forced_value = True

                    continue

            if forced_value:

                values.append(arg)

                continue

            m = re.match(r'(-+)([^=]+)', arg)

            if m:

                hyphens         =   m.group(1)
                given_label     =   m.group(2)
                given_name      =   hyphens + given_label
                resolved_name   =   given_name
                argument_alias  =   None
                given_hyphens   =   len(hyphens)
                extras          =   None

                gr              =   m.group()

                if gr != arg:

                    value       =   arg[1 + len(gr):]
                    option      =   Option(arg, index, given_name, resolved_name, argument_alias, given_hyphens, given_label, value, extras)

                    options.append(option)
                else:

                    flag        =   Flag(arg, index, given_name, resolved_name, argument_alias, given_hyphens, given_label, extras)

                    flags.append(flag)
            else:

                values.append(arg)

        return flags, options, values


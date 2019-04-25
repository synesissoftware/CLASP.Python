
from .specification import Specification
from .flag_specification import FlagSpecification
from .flag_argument import FlagArgument
from .option_specification import OptionSpecification
from .option_argument import OptionArgument

from .util import _get_program_name

import re

class Arguments:
    """Represents a parsed command-line, separated into program-name, flags, options, and values"""

    def __init__(self, argv, specifications = None):
        """Initialises an instance from the given argv and specifications sequences"""

        if not isinstance(argv, ( list, tuple )):

            raise TypeError("'argv' argument must be an instance of 'list' or 'tuple'")

        if specifications and not isinstance(specifications, ( list, tuple )):

            raise TypeError("'specifications' argument must be None or an instance of 'list' or 'tuple'")


        self.argv       =   argv

        self.specifications    =   specifications if specifications else ()

        flags, options, values  =   Arguments._parse(argv, self.specifications)

        self.program_name   =   _get_program_name(argv, {})
        """The program name"""

        self.flags      =   tuple(flags)
        """The parsed flags"""

        self.options    =   tuple(options)
        """The parsed options"""

        self.values     =   tuple(values)
        """The parsed values"""

    def aliases(self):
        "[DEPRECATED] instead use 'specifications'"""

        return self.specifications


    def flagIsSpecified(self, id):
        """Returns true if the given flag (name, or instance) has been specified; false otherwise"""

        return None != self.lookupFlag(id);

    def lookupFlag(self, id):
        """Looks and returns the identified flag from the instance's flags; returns None if not found"""

        name    =   None

        if False:

            pass
        elif FlagArgument == type(id):

            name    =   id.name
        elif OptionArgument == type(id):

            name    =   id.name
        else:

            name    =   id

        for index, flag in enumerate(self.flags):

            if flag.name == name:

                flag.use()

                return flag

        return None

    def lookupOption(self, id):
        """Looks and returns the identified option from the instance's options; returns None if not found"""

        name    =   None

        if False:

            pass
        elif FlagArgument == type(id):

            name    =   id.name
        elif OptionArgument == type(id):

            name    =   id.name
        else:

            name    =   id

        for index, option in enumerate(self.options):

            if option.name == name:

                option.use()

                return option

        return None

    def getFirstUnusedFlag(self):
        """Looks and returns the first unused flag from the instance's flags; returns None if not found"""

        for flag in self.flags:

            if not flag.used():

                return flag

        return None

    def getFirstUnusedOption(self):
        """Looks and returns the first unused option from the instance's options; returns None if not found"""

        for option in self.options:

            if not option.used():

                return option

        return None


    def getFirstUnusedFlagOrOption(self):

        flag    =   self.getFirstUnusedFlag()
        option  =   self.getFirstUnusedOption()

        if flag:

            if option:

                if flag.given_index < option.given_index:

                    return flag
                else:

                    return option
            else:

                return flag
        else:

            return option


    @staticmethod
    def _select_specification(item, specifications):

        for a in specifications:

            if a.name == item:

                return a

            for a2 in a.aliases:

                if item == a2:

                    return a

        return None

    @staticmethod
    def _select_specifications(item, specifications):

        select_specification = Arguments._select_specification(item, specifications)

        if select_specification:

            return select_specification

        n = len(item) - 1

        if n > 1:

            m = re.match(r'-+([a-zA-Z]+)$', item)

            if m:

                select_specifications  =   []

                for c in m.group(1):

                    name = '-' + c

                    select_specification = Arguments._select_specification(name, specifications)

                    if select_specification:

                        m2 = re.match(r'(-+)([^=]+)=(.*)$', select_specification.name)

                        if m2:

                            name2 = m2.group(1) + m2.group(2)

                            select_option_specification = Arguments._select_specification(name2, specifications)

                            if select_option_specification:

                                select_specifications.append((select_option_specification, select_specification, m2.group(3)))
                        else:

                            select_specifications.append(select_specification)


                if len(select_specifications) == n:

                    return select_specifications

        return None


    @staticmethod
    def _parse(argv, specifications):

        flags           =   []
        options         =   []
        values          =   []

        forced_value    =   False
        current_option  =   None

        for index, arg in enumerate(argv):

            if 0 == index:

                # ignore program name
                continue

            if not forced_value:

                if '--' == arg:

                    forced_value = True

                    continue

            if current_option:

                current_option.value    =   arg

                options.append(current_option)

                current_option          =   None

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
                arg_spec        =   None
                extras          =   None
                value           =   None
                is_option       =   False

                gr              =   m.group()

                if gr != arg:

                    # The option has an attached value

                    value       =   arg[1 + len(gr):]
                    is_option   =   True
                else:

                    # an option name, or a flag, or a combined set of flags

                    sel_specifications =   Arguments._select_specifications(arg, specifications)

                    if sel_specifications:

                        if isinstance(sel_specifications, (Specification, )):

                            pass
                        else:

                            # We have a combination of items

                            for a in sel_specifications:

                                if False:

                                    pass
                                elif isinstance(a, (FlagSpecification, )):

                                    flag = FlagArgument(arg, index, arg, a.name, a, len(hyphens), given_label, a.extras)

                                    flags.append(flag)
                                elif isinstance(a, (OptionSpecification, )):

                                    pass
                                elif isinstance(a, (tuple, )):

                                    soa =   a[0]
                                    fa  =   a[1]
                                    v   =   a[2]

                                    option = OptionArgument(arg, index, arg, soa.name, soa, len(hyphens), given_label, v, extras)

                                    options.append(option)
                                else:

                                    pass

                                pass

                            continue

                # Now look through the specifications, for:
                #
                # - the resolved name, and
                # - the default value, if none was attached
                for i, a in enumerate(specifications):

                    if a.name == given_name or given_name in a.aliases:

                        is_option       =   isinstance(a, OptionSpecification)

                        resolved_name   =   a.name
                        arg_spec        =   a
                        extras          =   a.extras

                        hyphens_2       =   None
                        given_label_2   =   None
                        value_2         =   None
                        resolved_name_2 =   None

                        alias_has_value =   False

                        m2 = re.match(r'(-+)([^=]+)=(.*)', resolved_name)

                        # need to check whether the alias is a
                        # valued-option, and, if so, expand out its name
                        # and value, and replace the name and (if not
                        # previously specified) the value

                        if m2:

                            alias_has_value =   True

                            hyphens_2       =   m2.group(1)
                            given_label_2   =   m2.group(2)
                            value_2         =   m2.group(3)
                            resolved_name_2 =   hyphens_2 + given_label_2

                            resolved_name   =   resolved_name_2

                            # now find the underlying (option) specification

                            for j, s2 in enumerate(specifications):

                                if s2.name == resolved_name or resolved_name in s2.aliases:

                                    arg_spec = s2

                                    break

                        if is_option:

                            if value != None:

                                if alias_has_value:



                                    value   =   value_2
                                else:

                                    if a.default_value:

                                        value   =   a.default_value
                        else:

                            if alias_has_value:

                                is_option   =   True
                                value       =   value_2

                        break

                if is_option:

                    option      =   OptionArgument(arg, index, given_name, resolved_name, arg_spec, len(hyphens), given_label, value, extras)

                    if value:

                        options.append(option)
                    else:

                        current_option  =   option
                else:

                    flag        =   FlagArgument(arg, index, given_name, resolved_name, arg_spec, len(hyphens), given_label, extras)

                    flags.append(flag)
            else:

                values.append(arg)

        if current_option:

            value   =   None
            specification   =   current_option.argument_specification

            if specification:

                if specification.default_value:

                    current_option.value = specification.default_value

            options.append(current_option)


        return flags, options, values


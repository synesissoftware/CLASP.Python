
from .specification import Specification
from .flag_specification import FlagSpecification
from .flag_argument import FlagArgument
from .option_specification import OptionSpecification
from .option_argument import OptionArgument

from .util import _get_program_name
from .util import _global_multiple_flags_action, _global_multiple_options_action
from .util import _MULTIPLE_ACTION_ALLOW, _MULTIPLE_ACTION_IGNORE, _MULTIPLE_ACTION_REJECT, _MULTIPLE_ACTION_REPLACE

import re
import sys

class Arguments:
    """Represents a parsed command-line, separated into program-name, flags, options, and values"""

    def __init__(self, argv, specifications = None):
        """Initialises an instance from the given argv and specifications sequences. Users should instead use clasp.parse()"""

        if not isinstance(argv, ( list, tuple )):

            raise TypeError("'argv' argument must be an instance of 'list' or 'tuple'")

        if specifications and not isinstance(specifications, ( list, tuple )):

            raise TypeError("'specifications' argument must be None or an instance of 'list' or 'tuple'")

        self.argv       =   argv

        self.specifications     =   specifications if specifications else ()

        flags, options, values  =   Arguments._parse(argv, self.specifications)

        self.program_name       =   Arguments.get_program_name(argv)
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
        """[DEPRECATED] Use flag_is_specified()"""

        return self.flag_is_specified(id)

    def flag_is_specified(self, id):
        """Returns true if the given flag (name, or instance) has been specified; false otherwise"""

        return None != self.lookup_flag(id);

    def lookupFlag(self, id):
        """[DEPRECATED] Use lookup_flag()"""

        return self.lookup_flag(id)

    def lookup_flag(self, id):
        """Looks and returns the identified flag from the instance's flags; returns None if not found"""

        name    =   None

        if False:

            pass
        elif FlagSpecification == type(id):

            name    =   id.name
        elif OptionSpecification == type(id):

            name    =   id.name
        else:

            name    =   id

        for index, flag in enumerate(self.flags):

            if flag.name == name:

                flag.use()

                return flag

        return None

    def lookupOption(self, id):
        """[DEPRECATED] Use lookup_option()"""

        return self.lookup_option(id)

    def lookup_option(self, id):
        """Looks and returns the identified option from the instance's options; returns None if not found"""

        name    =   None

        if False:

            pass
        elif FlagSpecification == type(id):

            name    =   id.name
        elif OptionSpecification == type(id):

            name    =   id.name
        else:

            name    =   id

        for index, option in enumerate(self.options):

            if option.name == name:

                option.use()

                return option

        return None

    def getFirstUnusedFlag(self):
        """[DEPRECATED] Use get_first_unused_flag()"""

        return self.get_first_unused_flag()

    def get_first_unused_flag(self, id=None):
        """Looks and returns the first unused flag from the instance's flags; returns None if not found

        If the argument `id` is specified, only matching unused flags will be obtained
        """

        for flag in self.flags:

            if id and not Arguments._id_matches(flag, id):

                continue

            if not flag.used():

                return flag

        return None

    def getFirstUnusedOption(self):
        """[DEPRECATED] Use get_first_unused_option()"""

        return self.get_first_unused_option()

    def get_first_unused_option(self, id=None):
        """Looks and returns the first unused option from the instance's options; returns None if not found

        If the argument `id` is specified, only matching unused options will be obtained
        """

        for option in self.options:

            if id and not Arguments._id_matches(option, id):

                continue

            if not option.used():

                return option

        return None


    def getFirstUnusedFlagOrOption(self):
        """[DEPRECATED] Use get_first_unused_flag_or_option()"""

        return self.get_first_unused_flag_or_option()

    def get_first_unused(self, id=None):
        """shorthand for get_first_unused_flag_or_option()"""

        return self.get_first_unused_flag_or_option(id)

    def get_first_unused_flag_or_option(self, id=None):
        """Obtains a reference to the first unused flag or option, or None if all no unused are found

        If the argument `id` is specified, only matching unused flags/options will be obtained
        """

        flag    =   self.get_first_unused_flag(id)
        option  =   self.get_first_unused_option(id)

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
    def _id_matches(flag_or_option, id):

        name    =   None

        if False:

            pass
        elif FlagSpecification == type(id):

            name    =   id.name
        elif OptionSpecification == type(id):

            name    =   id.name
        else:

            name    =   id

        return name == flag_or_option.name

    @staticmethod
    def get_program_name(argv=None):
        """Obtains/infers the program name from the given array, or from sys.argv"""

        if argv is None:

            argv = sys.argv

        return _get_program_name(argv, {})


    @staticmethod
    def _select_specification(item, specifications):

        for spec in specifications:

            if spec.name == item:

                return spec

            for a2 in spec.aliases:

                if item == a2:

                    return spec

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
    def _add_flag(flags, flag, spec):

        for i, f in enumerate(flags):

            if f == flag:

                default_action  =   _global_multiple_flags_action()

                if False:

                    pass
                elif _MULTIPLE_ACTION_IGNORE == default_action:

                    return
                elif _MULTIPLE_ACTION_REJECT == default_action:

                    raise DuplicateFlagSpecified(f, flag, spec)
                elif _MULTIPLE_ACTION_REPLACE == default_action:

                    flags[i] = flag

                    return

        flags.append(flag)

    @staticmethod
    def _add_option(options, option, spec):

        for i, o in enumerate(options):

            if o == option:

                action  =   None

                if not spec:

                    spec    =   option.argument_specification

                if spec:

                    action  =   spec.on_multiple
                else:

                    action  =   _global_multiple_options_action()

                if False:

                    pass
                elif _MULTIPLE_ACTION_ALLOW == action:

                    options.append(option)

                    return
                elif _MULTIPLE_ACTION_IGNORE == action:

                    return
                elif _MULTIPLE_ACTION_REJECT == action:

                    raise DuplicateOptionSpecified(o, option, spec)
                elif _MULTIPLE_ACTION_REPLACE == action:

                    options[i] = option

                    return

        options.append(option)

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

                current_option._set_value(arg)

                Arguments._add_option(options, current_option, None)

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

                            for spec in sel_specifications:

                                if False:

                                    pass
                                elif isinstance(spec, (FlagSpecification, )):

                                    flag = FlagArgument(arg, index, arg, spec.name, spec, len(hyphens), given_label, spec.extras)

                                    Arguments._add_flag(flags, flag, spec)
                                elif isinstance(spec, (OptionSpecification, )):

                                    pass
                                elif isinstance(spec, (tuple, )):

                                    soa =   spec[0]
                                    fa  =   spec[1]
                                    v   =   spec[2]

                                    option = OptionArgument(arg, index, arg, soa.name, soa, len(hyphens), given_label, v, extras)

                                    Arguments._add_option(options, option, soa)
                                else:

                                    pass

                                pass

                            continue

                # Now look through the specifications, for:
                #
                # - the resolved name, and
                # - the default value, if none was attached
                for i, spec in enumerate(specifications):

                    if spec.name == given_name or given_name in spec.aliases:

                        is_option       =   isinstance(spec, OptionSpecification)

                        resolved_name   =   spec.name
                        arg_spec        =   spec
                        extras          =   spec.extras

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

                                    if spec.default_value:

                                        value   =   spec.default_value
                        else:

                            if alias_has_value:

                                is_option   =   True
                                value       =   value_2

                        break

                if is_option:

                    option      =   OptionArgument(arg, index, given_name, resolved_name, arg_spec, len(hyphens), given_label, value, extras)

                    if value:

                        Arguments._add_option(options, option, arg_spec)
                    else:

                        current_option  =   option
                else:

                    flag        =   FlagArgument(arg, index, given_name, resolved_name, arg_spec, len(hyphens), given_label, extras)

                    Arguments._add_flag(flags, flag, arg_spec)
            else:

                values.append(arg)

        if current_option:

            value   =   None
            spec    =   current_option.argument_specification

            if spec:

                # always push, so value type processing can be done (for missing values)

                current_option._set_value(spec.default_value)

            Arguments._add_option(options, current_option, spec)


        return flags, options, values


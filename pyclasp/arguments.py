
from .alias import Alias
from .flag_alias import FlagAlias
from .flag_argument import FlagArgument
from .option_alias import OptionAlias
from .option_argument import OptionArgument

from .cli import _get_program_name

import re

class Arguments:

    def __init__(self, argv, aliases = None):

        if not isinstance(argv, ( list, tuple )):

            raise TypeError("'argv' argument must be an instance of 'list' or 'tuple'")

        if aliases and not isinstance(aliases, ( list, tuple )):

            raise TypeError("'aliases' argument must be None or an instance of 'list' or 'tuple'")


        self.argv       =   argv

        self.aliases    =   aliases if aliases else ()

        flags, options, values  =   Arguments._parse(argv, self.aliases)

        self.program_name   =   _get_program_name({})

        self.flags      =   tuple(flags)
        """The parsed flags"""

        self.options    =   tuple(options)
        """The parsed options"""

        self.values     =   tuple(values)
        """The parsed values"""

    def flagIsSpecified(self, id):

        return None != self.lookupFlag(id);

    def lookupFlag(self, id):

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

        for flag in self.flags:

            if not flag.used():

                return flag

        return False

    def getFirstUnusedOption(self):

        for option in self.options:

            if not option.used():

                return option

        return False


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
    def _select_alias(item, aliases):

        for a in aliases:

            if a.name == item:

                return a

            for a2 in a.aliases:

                if item == a2:

                    return a

        return None

    @staticmethod
    def _select_aliases(item, aliases):

        select_alias = Arguments._select_alias(item, aliases)

        if select_alias:

            return select_alias

        n = len(item) - 1

        if n > 1:

            m = re.match(r'-+([a-zA-Z]+)$', item)

            if m:

                select_aliases  =   []

                for c in m.group(1):

                    name = '-' + c

                    select_alias = Arguments._select_alias(name, aliases)

                    if select_alias:

                        m2 = re.match(r'(-+)([^=]+)=(.*)$', select_alias.name)

                        if m2:

                            name2 = m2.group(1) + m2.group(2)

                            select_option_alias = Arguments._select_alias(name2, aliases)

                            if select_option_alias:

                                select_aliases.append((select_option_alias, select_alias, m2.group(3)))
                        else:

                            select_aliases.append(select_alias)


                if len(select_aliases) == n:

                    return select_aliases

        return None


    @staticmethod
    def _parse(argv, aliases):

        flags           =   []
        options         =   []
        values          =   []

        forced_value    =   False
        current_option  =   None

        for index, arg in enumerate(argv):

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
                argument_alias  =   None
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

                    sel_aliases =   Arguments._select_aliases(arg, aliases)

                    if sel_aliases:

                        if isinstance(sel_aliases, (Alias, )):

                            pass
                        else:

                            # We have a combination of items

                            for a in sel_aliases:

                                if False:

                                    pass
                                elif isinstance(a, (FlagAlias, )):

                                    flag = FlagArgument(arg, index, arg, a.name, a, len(hyphens), given_label, a.extras)

                                    flags.append(flag)
                                elif isinstance(a, (OptionAlias, )):

                                    pass
                                elif isinstance(a, (tuple, )):

                                    soa =   a[0]
                                    fa  =   a[1]
                                    v   =   a[2]

                                    option = OptionArgument(arg, index, arg, soa.name, fa, len(hyphens), given_label, v, extras)

                                    options.append(option)
                                else:

                                    pass

                                pass

                            continue

                # Now look through the aliases, for:
                #
                # - the resolved name, and
                # - the default value, if none was attached
                for i, a in enumerate(aliases):

                    if a.name == given_name or given_name in a.aliases:

                        is_option       =   isinstance(a, OptionAlias)

                        resolved_name   =   a.name
                        argument_alias  =   a
                        extras          =   a.extras

                        hyphens_2       =   None
                        given_label_2   =   None
                        value_2         =   None
                        resolved_name_2 =   None

                        alias_has_value =   False

                        m2 = re.match(r'(-+)([^=]+)=(.*)', resolved_name)

                        if m2:

                            alias_has_value =   True

                            hyphens_2       =   m2.group(1)
                            given_label_2   =   m2.group(2)
                            value_2         =   m2.group(3)
                            resolved_name_2 =   hyphens_2 + given_label_2

                            resolved_name   =   resolved_name_2

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

                    option      =   OptionArgument(arg, index, given_name, resolved_name, argument_alias, len(hyphens), given_label, value, extras)

                    if value:

                        options.append(option)
                    else:

                        current_option  =   option
                else:

                    flag        =   FlagArgument(arg, index, given_name, resolved_name, argument_alias, len(hyphens), given_label, extras)

                    flags.append(flag)
            else:

                values.append(arg)

        if current_option:

            value   =   None
            alias   =   current_option.argument_alias

            if alias:

                if alias.default_value:

                    current_option.value = alias.default_value

            options.append(current_option)


        return flags, options, values


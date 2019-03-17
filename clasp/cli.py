
from .alias import Alias
from .util import dict_get_N

from .alias import Alias
from .flag_alias import FlagAlias
from .option_alias import OptionAlias

import os
import re
import sys

def _get_program_name(options):

    program_name    =   dict_get_N(options, 'program_name', 'program-name')

    if not program_name:

        bn      =   os.path.basename(sys.argv[0])

        program_name    =   bn

    return program_name

def _generate_version_string(options):

    program_name    =   _get_program_name(options)
    version_prefix  =   dict_get_N((options, ''), 'version_prefix', 'version-prefix')

    version         =   options.get('version')

    if version:

        if isinstance(version, (list, tuple, )):

            version =   [ str(i) for i in version ]

            version =   '.'.join(version)
    else:

        version_major   =  dict_get_N(options, 'version_major', 'version-major')

        if not version_major:

            raise ValueError("options must specify 'version' or 'version_major' [ + 'version_minor' [ + [ 'version_patch' (or 'version_revision') [ + 'version_build' ] ] ] ")

        version_minor   =   dict_get_N(options, 'version_minor', 'version-minor')
        version_patch   =   dict_get_N(options, 'version_patch', 'version-patch', 'version_revision', 'version-revision')
        version_build   =   dict_get_N(options, 'version_build', 'version-build')

        version         =   str(version_major)

        if version_minor:

            version     +=  '.' + str(version_minor)

        if version_patch:

            version     +=  '.' + str(version_patch)

        if version_build:

            version     +=  '.' + str(version_build)

    return "%s %s%s" % (program_name, version_prefix, version)


def show_usage(aliases, **kwargs):

    if __debug__:

        if aliases == None:

            raise TypeError("'aliases' may not be None")
        elif isinstance(aliases, (list, tuple, )):

            for index, a in enumerate(aliases):

                if not isinstance(a, (Alias, )):

                    raise TypeError("every element in 'aliases' must be an instance of clasp.Alias: the element at index %d is of type '%s'" % (index, type(a).__name__))
        else:

            raise TypeError("'aliases' must be a list or a tuple")

    options             =   kwargs

    exit_code           =   dict_get_N(options, 'exit', 'exit_code', 'exit-code')
    flags_and_options   =   dict_get_N((options, ' [ ... flags and options ... ]'), 'flags_and_options', 'flags-and-options')
    info_lines          =   dict_get_N(options, 'info_lines', 'info-lines')
    program_name        =   _get_program_name(options)
    stream              =   dict_get_N((options, sys.stdout), 'stream')
    suppress_blanks     =   dict_get_N(options, 'suppress_blank_lines_between_options', 'suppress-blank-lines-between-options')
    values              =   options.get('values', '')

    if not info_lines:

        info_lines  =   []
    elif isinstance(info_lines, (list, tuple, )):

        pass
    else:

        info_lines  =   [ info_lines ]

    info_lines      =   [ _generate_version_string(options) if l in ( ':version', ':version:' ) else l for l in info_lines ]


    # sift the aliases to sort out which are value-option aliases (VOAs)

    pure_aliases    =   []
    voas            =   {}

    for alias in aliases:

        m       =   re.match(r'(-+[a-zA-Z0-3_-]+)[=:](.+)$', alias.name)

        if m:

            name    =   m.group(1)
            value   =   m.group(2)

            if not voas.get(name):

                voas[name] = []

            voas[name].append([ alias, value ])
        else:

            pure_aliases.append(alias)

    aliases         =   pure_aliases


    for info_line in info_lines:

        stream.write("%s\n" % info_line)

    stream.write("USAGE: %s%s%s\n\n" % (program_name, flags_and_options, values))

    if aliases:

        stream.write("flags/options:\n\n")

        for alias in aliases:

            if isinstance(alias, FlagAlias):

                for a2 in alias.aliases:

                    stream.write("\t%s\n" % a2)

                stream.write("\t%s\n" % alias.name)
                stream.write("\t\t%s\n" % alias.help)
            elif isinstance(alias, OptionAlias):

                voa = voas.get(alias.name)

                if voa:

                    for a2 in voa:

                        for a3 in a2[0].aliases:

                            stream.write("\t%s %s\n" % (a3, a2[0].name))

                for a2 in alias.aliases:

                    stream.write("\t%s <value>\n" % a2)

                stream.write("\t%s=<value>\n" % alias.name)
                stream.write("\t\t%s\n" % alias.help)
                if alias.values_range:

                    stream.write("\t\twhere <value> one of:\n")

                    for v in alias.values_range:

                        stream.write("\t\t\t%s\n" % v)

            elif isinstance(alias, Alias):

                pass
            else:

                pass

            if not suppress_blanks:

                stream.write("\n")

    if None != exit_code:

        sys.exit(exit_code)



def show_version(aliases, **kwargs):

    if __debug__:

        if aliases == None:

            raise TypeError("'aliases' may not be None")
        elif isinstance(aliases, (list, tuple, )):

            for index, a in enumerate(aliases):

                if not isinstance(a, (Alias, )):

                    raise TypeError("every element in 'aliases' must be an instance of clasp.Alias: the element at index %d is of type '%s'" % (index, type(a).__name__))
        else:

            raise TypeError("'aliases' must be a list or a tuple")

    # options:
    #
    # - exit (integer, or None)
    # - program_name (string)
    # - stream (file, ...)
    # - version (array) or
    # - version_major, version_minor, version_patch or version_revision, version_build (all integer)
    # - version_prefix (string)

    exit_code       =   kwargs.get('exit', kwargs.get('exit_code', kwargs.get('exit-code')))
    stream          =   kwargs.get('stream', sys.stdout)

    version         =   _generate_version_string(kwargs)

    stream.write("%s\n" % version)

    if None != exit_code:

        sys.exit(exit_code)


# ############################## end of file ############################# #



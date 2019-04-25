
from .arguments import Arguments
from .util import _dict_get_N, _get_program_name

from .specification import Specification
from .flag_specification import FlagSpecification
from .option_specification import OptionSpecification

import os
import re
import sys

def _generate_version_string(argv, options):

    program_name    =   _get_program_name(argv, options)
    version_prefix  =   _dict_get_N((options, ''), 'version_prefix', 'version-prefix')

    version         =   options.get('version')

    if version:

        if isinstance(version, (list, tuple, )):

            version =   [ str(i) for i in version ]

            version =   '.'.join(version)
    else:

        version_major   =  _dict_get_N(options, 'version_major', 'version-major')

        if not version_major:

            raise ValueError("options must specify 'version' or 'version_major' [ + 'version_minor' [ + [ 'version_patch' (or 'version_revision') [ + 'version_build' ] ] ] ")

        version_minor   =   _dict_get_N(options, 'version_minor', 'version-minor')
        version_patch   =   _dict_get_N(options, 'version_patch', 'version-patch', 'version_revision', 'version-revision')
        version_build   =   _dict_get_N(options, 'version_build', 'version-build')

        version         =   str(version_major)

        if version_minor:

            version     +=  '.' + str(version_minor)

        if version_patch:

            version     +=  '.' + str(version_patch)

        if version_build:

            version     +=  '.' + str(version_build)

    return "%s %s%s" % (program_name, version_prefix, version)


def show_usage(specifications, **kwargs):
    """Displays program usage from the given specifications (or arguments), according to the given options"""

    argv                =   sys.argv

    if isinstance(specifications, (Arguments, )):

        args            =   specifications
        argv            =   args.argv
        specifications  =   args.specifications

    if __debug__:

        if specifications == None:

            raise TypeError("'specifications' may not be None")
        elif isinstance(specifications, (list, tuple, )):

            for index, a in enumerate(specifications):

                if not isinstance(a, (Specification, )):

                    raise TypeError("every element in 'specifications' must be an instance of clasp.Specification: the element at index %d is of type '%s'" % (index, type(a).__name__))
        else:

            raise TypeError("'specifications' must be a list or a tuple")

    options             =   kwargs

    exit_code           =   _dict_get_N(options, 'exit', 'exit_code', 'exit-code')
    flags_and_options   =   _dict_get_N((options, ' [ ... flags and options ... ]'), 'flags_and_options', 'flags-and-options')
    info_lines          =   _dict_get_N(options, 'info_lines', 'info-lines')
    program_name        =   _get_program_name(argv, options)
    stream              =   _dict_get_N((options, sys.stdout), 'stream')
    suppress_blanks     =   _dict_get_N(options, 'suppress_blank_lines_between_options', 'suppress-blank-lines-between-options')
    values              =   options.get('values', '')

    if not info_lines:

        info_lines  =   []
    elif isinstance(info_lines, (list, tuple, )):

        pass
    else:

        info_lines  =   [ info_lines ]

    info_lines      =   [ _generate_version_string(argv, options) if l in ( ':version', ':version:' ) else l for l in info_lines ]


    # sift the specifications to sort out which are value-option aliases (VOAs)

    pure_specifications    =   []
    voas            =   {}

    for specification in specifications:

        m       =   re.match(r'(-+[a-zA-Z0-3_-]+)[=:](.+)$', specification.name)

        if m:

            name    =   m.group(1)
            value   =   m.group(2)

            if not voas.get(name):

                voas[name] = []

            voas[name].append([ specification, value ])
        else:

            pure_specifications.append(specification)

    specifications         =   pure_specifications


    for info_line in info_lines:

        stream.write("%s\n" % info_line)

    stream.write("USAGE: %s%s%s\n\n" % (program_name, flags_and_options, values))

    if specifications:

        stream.write("flags/options:\n\n")

        for specification in specifications:

            if isinstance(specification, FlagSpecification):

                for a2 in specification.aliases:

                    stream.write("\t%s\n" % a2)

                stream.write("\t%s\n" % specification.name)
                stream.write("\t\t%s\n" % specification.help)
            elif isinstance(specification, OptionSpecification):

                voa = voas.get(specification.name)

                if voa:

                    for a2 in voa:

                        for a3 in a2[0].aliases:

                            stream.write("\t%s %s\n" % (a3, a2[0].name))

                for a2 in specification.aliases:

                    stream.write("\t%s <value>\n" % a2)

                stream.write("\t%s=<value>\n" % specification.name)
                stream.write("\t\t%s\n" % specification.help)
                if specification.values_range:

                    stream.write("\t\twhere <value> one of:\n")

                    for v in specification.values_range:

                        stream.write("\t\t\t%s\n" % v)

            elif isinstance(specification, Specification):

                pass
            else:

                pass

            if not suppress_blanks:

                stream.write("\n")

    if None != exit_code:

        sys.exit(exit_code)



def show_version(specifications, **kwargs):
    """Displays program version from the given specifications (or arguments), according to the given options"""

    argv                =   sys.argv

    if isinstance(specifications, (Arguments, )):

        args            =   specifications
        argv            =   args.argv
        specifications  =   args.specifications

    if __debug__:

        if specifications == None:

            raise TypeError("'specifications' may not be None")
        elif isinstance(specifications, (list, tuple, )):

            for index, a in enumerate(specifications):

                if not isinstance(a, (Specification, )):

                    raise TypeError("every element in 'specifications' must be an instance of clasp.Specification: the element at index %d is of type '%s'" % (index, type(a).__name__))
        else:

            raise TypeError("'specifications' must be a list or a tuple")

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

    version         =   _generate_version_string(argv, kwargs)

    stream.write("%s\n" % version)

    if None != exit_code:

        sys.exit(exit_code)


# ############################## end of file ############################# #



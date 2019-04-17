
import os

def _dict_get_N(d, *keys):

    default =   None

    if isinstance(d, (tuple, )):

        default =   d[1]
        d       =   d[0]

    for key in keys:

        if key in d:

            return d.get(key)

    return default

def _get_program_name(argv, options):

    program_name    =   _dict_get_N(options, 'program_name', 'program-name')

    if not program_name:

        bn              =   os.path.basename(argv[0])

        program_name    =   bn

    return program_name


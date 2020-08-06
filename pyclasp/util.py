
import os

_MULTIPLE_ACTION_ALLOW      =   'ALLOW'
_MULTIPLE_ACTION_IGNORE     =   'IGNORE'
_MULTIPLE_ACTION_REJECT     =   'REJECT'
_MULTIPLE_ACTION_REPLACE    =   'REPLACE'

_MULTIPLE_ACTION_FLAG_ALLOWED = (

    _MULTIPLE_ACTION_IGNORE,
    _MULTIPLE_ACTION_REJECT,
    _MULTIPLE_ACTION_REPLACE,
)

_MULTIPLE_ACTION_OPTION_ALLOWED = (

    _MULTIPLE_ACTION_ALLOW,
    _MULTIPLE_ACTION_IGNORE,
    _MULTIPLE_ACTION_REJECT,
    _MULTIPLE_ACTION_REPLACE,
)

_MULTIPLE_FLAG_ACTION_DEFAULT    =   _MULTIPLE_ACTION_REPLACE
_MULTIPLE_OPTION_ACTION_DEFAULT  =   _MULTIPLE_ACTION_ALLOW

def _dict_get_N(d, *keys, **kwargs):

    default         =   None
    default_if_none =   kwargs.get('default_if_none', False)


    if isinstance(d, (tuple, )):

        default =   d[1]
        d       =   d[0]

    for key in keys:

        if key in d:

            v = d.get(key)

            if None == v and default_if_none:

                continue

            return v

    return default

def _get_program_name(argv, options):

    program_name    =   _dict_get_N(options, 'program_name', 'program-name')

    if not program_name:

        bn              =   os.path.basename(argv[0])

        program_name    =   bn

    return program_name

def _global_multiple_flags_action():

    a = os.environ.get('CLASP_MULTIPLE_FLAG_ACTION')

    if a:

        a = a.upper()

    if a:

        if not a in _MULTIPLE_ACTION_FLAG_ALLOWED:

            a = None

    if not a:

        a = _MULTIPLE_FLAG_ACTION_DEFAULT

    return a


def _global_multiple_options_action():

    a = os.environ.get('CLASP_MULTIPLE_OPTION_ACTION')

    if a:

        a = a.upper()

    if a:

        if not a in _MULTIPLE_ACTION_OPTION_ALLOWED:

            a = None

    if not a:

        a = _MULTIPLE_OPTION_ACTION_DEFAULT

    return a



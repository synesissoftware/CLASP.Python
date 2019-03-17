
def dict_get_N(d, *keys):

    default =   None

    if isinstance(d, (tuple, )):

        default =   d[1]
        d       =   d[0]

    for key in keys:

        if key in d:

            return d.get(key)

    return default


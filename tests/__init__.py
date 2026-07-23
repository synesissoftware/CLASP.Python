# This file present to deal with warnings from packager

import sys

if sys.version_info[0] < 3:

    import unittest

    try:

        import mock

        sys.modules['unittest.mock'] = mock
    except ImportError:

        raise ImportError(
            "the 'mock' package is required to run tests on Python 2.7",
        )

    if not hasattr(unittest.TestCase, 'assertRegex'):

        unittest.TestCase.assertRegex = unittest.TestCase.assertRegexpMatches


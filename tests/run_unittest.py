#! /usr/bin/env python
"""
unittest entry point.

Imports the `tests` package first so tests/__init__.py can install
Python 2.7 compatibility shims before test modules load.
"""

import os
import sys
import unittest


def main():

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if root not in sys.path:

        sys.path.insert(0, root)

    import tests  # noqa: F401

    start_dir = os.path.join(root, 'tests')
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir,
        pattern='test_*.py',
        top_level_dir=root,
    )
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    sys.exit(0 if result.wasSuccessful() else 1)


if '__main__' == __name__:

    main()

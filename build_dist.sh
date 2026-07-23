#! /bin/bash

set -e

cd "$(dirname "$0")"

rm -rf build/ dist/ clasp.egg-info/

python3 -m build
python3 -m twine check dist/*

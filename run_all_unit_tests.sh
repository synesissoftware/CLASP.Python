#! /bin/bash

Source="${BASH_SOURCE[0]}"
while [ -h "$Source" ]; do

  Dir="$(cd -P "$(dirname "$Source")" && pwd)"
  Source="$(readlink "$Source")"
  [[ $Source != /* ]] && Source="$Dir/$Source"
done
Dir="$(cd -P "$( dirname "$Source" )" && pwd)"

# This will operate recursively as long as each subdirectory of $Dir/tests
# contains an __init__.py file (which may be empty)
python3 "$Dir/tests/run_unittest.py"

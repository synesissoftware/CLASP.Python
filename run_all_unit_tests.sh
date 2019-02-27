#!/bin/bash

#############################################################################
# File:         run_all_unit_tests.sh
#
# Purpose:      Executes the unit-tests regardless of calling directory
#
# Created:      13th February 2019
# Updated:      13th February 2019
#
# Author:       Matthew Wilson
#
#############################################################################

source="${BASH_SOURCE[0]}"
while [ -h "$source" ]; do
  dir="$(cd -P "$(dirname "$source")" && pwd)"
  source="$(readlink "$source")"
  [[ $source != /* ]] && source="$dir/$source"
done
dir="$( cd -P "$( dirname "$source" )" && pwd )"

[[ -d "$dir/test" ]] && find $dir/test -name '*.py' -exec python {} \;
[[ -d "$dir/tests" ]] && find $dir/tests -name '*.py' -exec python {} \;



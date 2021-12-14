#!/usr/bin/env bash
# list of test cases to run:
tests=(
	lib/test_earthDistances.py
)

# decide what driver to use (depending on arguments given)
unit='-m unittest'
if [[ $# -gt 0 && ${1} == 'coverage' ]]; then
#       driver="${@} ${unit}"
       driver="coverage run -m pytest"
       report="coverage report -m"
elif [[ $# -gt 0 && ${1} == 'pytest'* ]]; then
       driver="${@}"
       report=""
else
       driver="python ${@} ${unit}"
       report=""
fi
 
# we must add the module source path because we use `import cs107_package` in our test suite and we
# want to test from the source directly (not a package that we have (possibly) installed earlier)
export PYTHONPATH="$(pwd -P)/../src/":${PYTHONPATH}
 
# run the tests
${driver} ${tests[@]}
${report}

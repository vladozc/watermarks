#!/bin/bash

function install_environment()
{
    local e=e_$1
    if [ "$clean" -eq 1 ]; then
        rm -rf $e
    fi
    if [ ! -d "$e" ]; then
        virtualenv -p $1 $e
        $e/bin/pip install -r requirements.txt
    fi
}

function run_tests()
{
    local e=e_$1
    PYTHONPATH=src:utils $e/bin/nosetests test/functiontests/
}

clean=0

while getopts C o
do case "$o" in
    C) clean=1;;
    [?])
        echo >&2 "Usage: $0 [-C]"
        exit 1;;
    esac
done

for python in python2.6 python2.7 python3.0 python3.1 python3.2 python3.3 python3.4
do
    echo "##################"
    echo "Testing $python"
    type $python &> /dev/null
    if [ $? -eq 0 ]; then
        install_environment $python
        run_tests $python
    else
        echo "$python is not installed"
    fi
    echo
done

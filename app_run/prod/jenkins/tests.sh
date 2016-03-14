#!/bin/bash

set -ex
set -o pipefail

echo "****** Install new virtual env ******"
pwd

cd $WORKSPACE

test -e "$PWD/env" && rm -rf "$PWD/env"

virtualenv env

source env/bin/activate

pip install -r requirements.txt
pip install -r test_requirements.txt


echo "***********************"

echo "****** Run tests ******"

coverage run --source='trololo' trololo/manage.py test trololo/ || { echo "Tests FAILED"; exit 1; }

percentage=$(coverage report | tail -n 1 | awk '{print $4}' | awk -F% '{print $1}')

coverage_limit=70

echo "Tests coverage % is - $percentage %"

[ $percentage -lt $coverage_limit ] && { echo "Coverage $percentage is LESS than $coverage_limit"; exit 1; }

echo "******** END ***********"

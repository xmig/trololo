#!/bin/bash

set -ex
set -o pipefail

echo "****** Install new virtual env ******"
pwd

git status

cd $WORKSPACE

test -e "$PWD/env" && rm -rf "$PWD/env"

virtualenv env

source env/bin/activate

pip install -r requirements.txt
pip install -r test_requirements.txt


echo "***********************"

echo "****** Run tests ******"

coverage run --source='trololo' --omit="*wsgi.py,*urls.py,*stage.py" trololo/manage.py test trololo/

coverage report --fail-under=70

echo "******** END ***********"
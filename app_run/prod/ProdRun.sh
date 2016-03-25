#!/bin/bash

set -ex

echo "++++++ Start Prod Project Script ++++++"

echo "------------------------------------------------------"
echo "User:"
whoami
echo "------------------------------------------------------"

echo "-------------------- Go to (APP home) --------------------"
cd /home/ubuntu/projects/trololo/prod/
pwd
echo "------------------------------------------------------"

echo "-== Activate Venv ==-"
source /home/ubuntu/projects/trololo/prod_venv/bin/activate
echo "------------------------------------------------------"

echo "-== Install python Packeges ==-"
pip install -r requirements.txt > /dev/null
sleep 1

export DJANGO_SETTINGS_MODULE="trololo.settings.production"
echo "#----------------------------------- Collection Static -----------------------------------#"
cd /home/ubuntu/projects/trololo/prod/trololo

python manage.py collectstatic --noinput
echo "#-------------------------------- Collection Static: END --------------------------------#"
echo "#-------------------------------- Apply Migrations --------------------------------#"
python manage.py migrate

echo "#-------------------------------- Apply Migrations: END --------------------------------#"

deactivate
echo "#----------------------------------- END Prod Project Script -----------------------------------#"

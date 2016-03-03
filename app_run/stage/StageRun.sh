#!/bin/bash

echo "++++++ Start Staging Project Script ++++++"

echo "------------------------------------------------------"
echo "User:"
whoami
echo "------------------------------------------------------"

echo "-------------------- Go to (APP home) --------------------"
cd /home/ubuntu/projects/trololo/
pwd
echo "------------------------------------------------------"

echo "-== Activate Venv ==-"
source /home/ubuntu/projects/trololo/venv/bin/activate
echo "------------------------------------------------------"

echo "-== Install python Packeges ==-"
pip install -r requirements.txt
sleep 1

export DJANGO_SETTINGS_MODULE="trololo.settings.stage"
#echo "#----------------------------------- Collection Static: NUCLEUS -----------------------------------#"
#cd /home/nucleus/www/Staging/nucleus/NUCLEUS
#./manage.py collectstatic --noinput
#echo "#-------------------------------- Collection Static: NUCLEUS: END --------------------------------#"

#echo "#----------------------------------- Collection Static: WEBSHOP -----------------------------------#"
#cd /home/nucleus/www/Staging/fragrantjewels/WEBSHOP
#./manage.py collectstatic --noinput
#echo "#-------------------------------- Collection Static: WEBSHOP: END --------------------------------#"

echo "#----------------------------------- END -----------------------------------#"

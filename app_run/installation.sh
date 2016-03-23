#!/bin/bash
set -ex
# RUN this script as superuser from PROJECT ROOT
if [ "${UID}" != 0 ]; then
    echo "This script must be run as root"
    exit 1
fi

if [ -f "$PWD/README.md" ]; then
    if [ -z "$(cat README.md | grep 'Task/Issue/Bug tracker')" ]; then
        echo "This script must be run from the project root"
        exit 1
    fi
else
    echo "This script must be run from the project root"
    exit 1
fi

# install required packages
sudo apt-get install python-dev python-pip postgresql-9.3 postgresql-server-dev-9.3

# allow postgres user login to DB
sudo sed -i 's/local   all             postgres                                peer/local   all             postgres                                trust/g' /etc/postgresql/9.3/main/pg_hba.conf
sudo sed -i 's/local   all             all                                     peer/#local   all             all                                     peer/g' /etc/postgresql/9.3/main/pg_hba.conf
sudo service postgresql reload

# add trololo/ dir to the PYTHONPATH
export PYTHONPATH="${PWD}/trololo/"

# get user, DB name and password from config
LOCAL_DB_USER=$(python -c "from trololo import settings; print settings.DATABASES['default']['USER']")
LOCAL_DB_NAME=$(python -c "from trololo import settings; print settings.DATABASES['default']['NAME']")
LOCAL_DB_PASSWORD=$(python -c "from trololo import settings; print settings.DATABASES['default']['PASSWORD']")

echo $LOCAL_DB_USER
echo $LOCAL_DB_NAME
echo $LOCAL_DB_PASSWORD

# create role and database
sudo psql -U postgres -c "CREATE ROLE ${LOCAL_DB_USER} LOGIN CREATEDB;"
sudo psql -U postgres -c "ALTER ROLE ${LOCAL_DB_USER} WITH PASSWORD '${LOCAL_DB_PASSWORD}';"
sudo psql -U postgres -c "CREATE DATABASE ${LOCAL_DB_NAME} OWNER ${LOCAL_DB_USER};"

sudo service postgresql restart

# enable password auth
sudo echo "local   all             ${LOCAL_DB_USER}                                md5" >> /etc/postgresql/9.3/main/pg_hba.conf
sudo sed -i 's/local   all             postgres                                trust/local   all             postgres                                peer/g' /etc/postgresql/9.3/main/pg_hba.conf
sudo service postgresql restart

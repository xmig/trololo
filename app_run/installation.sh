#!/bin/bash
#
# Script to install all required system packages on ubuntu
#

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

PROJ_DIR="${PWD}"

# install required packages
sudo apt-get update

sudo apt-get install redis-server libjpeg-dev zlib1g-dev python-dev python-pip

# Install and configure postgresql-server-9.3
INCORRECT=true;

while [ "$INCORRECT" = "true" ]; do
    read -p "Do you want to install and configure postgresql server? [Y|n]" RESP

    case "$RESP" in
        "n" | "no" | "N" | "No" ) INCORRECT=false; echo "Exiting ..."; exit 0;;
        "y" | "Y" | "Yes" | "yes" ) INCORRECT=false; echo "Configure postgresql server 9.3 ...";;
        * ) echo "Incorrect choice!";&
    esac
done

sudo apt-get install postgresql-9.3 postgresql-server-dev-9.3

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
sudo psql -U postgres -c "DROP DATABASE IF EXISTS ${LOCAL_DB_NAME};"
sudo psql -U postgres -c "DROP ROLE IF EXISTS ${LOCAL_DB_USER};"
sudo psql -U postgres -c "CREATE ROLE ${LOCAL_DB_USER} LOGIN CREATEDB PASSWORD '${LOCAL_DB_PASSWORD}';"
sudo psql -U postgres -c "CREATE DATABASE ${LOCAL_DB_NAME} OWNER ${LOCAL_DB_USER};"

sudo service postgresql restart

# enable password auth
sudo echo "local   all             ${LOCAL_DB_USER}                                md5" >> /etc/postgresql/9.3/main/pg_hba.conf
sudo sed -i 's/local   all             postgres                                trust/local   all             postgres                                peer/g' /etc/postgresql/9.3/main/pg_hba.conf
sudo service postgresql restart

##################
# Sphinx install #
##################
apt-get install -y postgresql-server-dev-all postgresql-common libmysqlclient-dev mysql-client-5.6

# Installing Sphinx is much easier from Sphinxsearch PPA repository, because you
# will get all dependencies and can also update Sphinx to the latest version with
# the same command.

# First, add Sphinxsearch repository and update the list of packages:

sudo add-apt-repository -y ppa:builds/sphinxsearch-rel22
sudo apt-get update

# Install/update sphinxsearch package:

sudo apt-get install -y sphinxsearch

# install pg_sphinx extension

cd ~ && git clone https://github.com/andy128k/pg-sphinx
cd pg-sphinx/
make && sudo make install

cd ${PROJ_DIR}

sudo cp /etc/sphinxsearch/sphinx.conf /etc/sphinxsearch/sphinx.conf.old
sudo cp search_server/Sphinx/search.conf /etc/sphinxsearch/sphinx.conf

sudo service sphinxsearch restart

echo 'CREATE EXTENSION sphinx;' | psql -U ${LOCAL_DB_USER} ${LOCAL_DB_NAME}

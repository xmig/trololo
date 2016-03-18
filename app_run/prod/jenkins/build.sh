#!/bin/bash

set -ex
set -o pipefail

echo "****** Start Jenkins Script Step #1 ******"

echo "*************** USER: ***************"
echo "User:"
whoami
cd /home/ubuntu/projects/trololo/prod/
pwd
git branch
sudo -u ubuntu git pull
echo "**************** End #1 *******************"

sudo supervisorctl stop trololo

echo "******** Jenkins Script Step #2 ********"

export BUILD=$BUILD_NUMBER

echo "****** Run StageRun.sh Script as User: ubuntu ******"

echo "*** Go to Scripts folder: /home/ubuntu/projects/trololo/app_run/prod/ ***"
cd /home/ubuntu/projects/trololo/prod/app_run/prod/

sudo -u ubuntu bash ProdRun.sh

echo "*** Restart supervisorctl and nginx ***"

sudo supervisorctl start trololo
sudo service nginx restart

#!/bin/bash

./re.sh

cp ../*.deb ~/ex/login-deploy
cd ~/ex/login-deploy && git add . && git commit -m "upadte loginserver.deb" && git push

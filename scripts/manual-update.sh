#!/bin/bash

git pull

rm ./Complete.conf
wget https://cdn.jsdelivr.net/gh/lhie1/Rules/Shadowrocket/Complete.conf
python3 ./scripts/merge-lhie1.py
python3 ./scripts/build-ad.py
python3 ./scripts/build-telegram.py
python3 ./scripts/build-direct.py
python3 ./scripts/build-proxy.py
python3 ./scripts/build-netease.py
python3 ./scripts/gen-final.py

git add .
git commit -m "manual update" -a
git push

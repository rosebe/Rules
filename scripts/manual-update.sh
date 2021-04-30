#!/bin/bash

rm ./Complete.conf
wget https://cdn.jsdelivr.net/gh/lhie1/Rules/Shadowrocket/Complete.conf
python ./scripts/merge-lhie1.py
python ./scripts/build-gfwlist.py
python ./scripts/build-ad.py
python ./scripts/build-telegram.py
python ./scripts/gen-gfw-ad-netease.py

git add .
git commit -m "manual update" -a
git push
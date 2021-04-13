#!/bin/bash

rm ./Complete.conf
rm ./sr_top500_banlist_ad.conf
wget https://cdn.jsdelivr.net/gh/lhie1/Rules/Shadowrocket/Complete.conf
wget https://h2y.github.io/Shadowrocket-ADBlock-Rules/sr_top500_banlist_ad.conf
python ./scripts/merge-h2y.py
python ./scripts/merge-lhie1.py

git config --global user.email xiangjianjian@aliyun.com
git config --global user.name Chien
git add .
git commit -m "update" -a
git push
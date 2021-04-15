#!/bin/bash

rm ./Complete.conf
wget https://cdn.jsdelivr.net/gh/lhie1/Rules/Shadowrocket/Complete.conf
python ./scripts/merge-lhie1.py

git config --global user.email xiangjianjian@aliyun.com
git config --global user.name Chien
git add .
git commit -m "update" -a
git push
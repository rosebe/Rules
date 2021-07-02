#!/bin/bash

git pull

python3 ./scripts/build-ad.py
python3 ./scripts/build-telegram.py
python3 ./scripts/build-direct.py
python3 ./scripts/build-proxy.py
python3 ./scripts/build-netease.py
python3 ./scripts/build-node.py
python3 ./scripts/merge-lhie1.py
python3 ./scripts/gen-final.py

git add .
git commit -m "manual update" -a
git push

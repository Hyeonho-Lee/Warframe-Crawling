#!/bin/bash

echo "===========업데이트를 시작하겠습니다.==========="
python3 index_v2.py

echo "===========업로드 준비를 하겠습니다.==========="
git status
git add -A
git commit -m "upload files"
git push origin master


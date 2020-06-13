#!/bin/bash
cd /workspace/crawling
echo "업데이트를 시작하겠습니다."
echo "워프레임 업데이트 중입니다....."
/usr/local/bin/python3 /workspace/crawling/python/warframes_update.py
echo "무기 업데이트 중입니다....."
/usr/local/bin/python3 /workspace/crawling/python/weapons_update.py
echo "기타 무기 업데이트 중입니다....."
/usr/local/bin/python3 /workspace/crawling/python/weapons_etc_update.py
echo "결산 중입니다....."
/usr/local/bin/python3 /workspace/crawling/python/today_recommend.py
echo "업데이트를 마쳤습니다."
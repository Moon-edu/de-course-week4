from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import json

# 아래에서 pass를 지우고 로직을 작성하세요(20점)
# 아래 함수를 실행하면, assets.json 파일에 있는 모든 레코드의 자산 평가액(est_asset_dollar)의 합계, 평균, 총 레코드 수를 리턴해야 합니다.
# 리턴 값의 예) (100391284324, 198312.8732, 500)
def summarize() -> Tuple:
    # data 읽어오기
    with open("hw_data/assets.json", "r") as json_file:
        data = json.load(json_file)
        
    # 자산 집계액 구하기
    sum_asset = sum(int(row['est_asset_dollar']) for row in data)
    avg_asset = sum_asset / len(data)
    cnt_asset = len(data)
        
    return (sum_asset, avg_asset, cnt_asset)

0from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import openpyxl

# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 Corp.로 끝나는 회사를 다니는 사람들의 자산 총 합계를 리턴합니다.
# 리턴 값의 예) 10239102305
def find_corp_total_asset() -> int:
    wb = openpyxl.load_workbook("hw_data/assets.xlsx")
    ws = wb.active

    flags = False
    sum_assets = 0

    # 로우만 가지고 오기
    for row in ws:
        if not flags:
            flags = True
        elif row[1].value.endswith('Corp.'):
            sum_assets += int(row[4].value)

    return sum_assets


# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 LLC로 끝나는 회사를 다니는 사람들의 자산 총 평균을 리턴합니다.
# 리턴 값의 예) 1025831.87653
def find_llc_total_asset() -> int:
    wb = openpyxl.load_workbook("hw_data/assets.xlsx")
    ws = wb.active
    sum = 0
    cnt = 0
    flags = False
    
    for row in ws:
        if not flags:
            flags = True
        elif row[1].value.endswith('LLC'):
            sum += int(row[4].value)
            cnt += 1

    if cnt > 0:
        return sum/cnt
    else:
        return 0


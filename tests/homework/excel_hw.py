from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import openpyxl

# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 Corp.로 끝나는 회사를 다니는 사람들의 자산 총 합계를 리턴합니다.
# 리턴 값의 예) 10239102305
def find_corp_total_asset() -> int:
    wb = openpyxl.load_workbook("/Users/eunalong/Documents/GitHub/start_de/de-course-week4/hw_data/assets.xlsx")
    ws = wb.active

    flags = False
    data = []

    # 로우만 가지고 오기
    for row in ws :
        if not flags :
            flags = True
            continue
        data.append({
            'name' : row[0].value,
            'company' : row[1].value,
            'city' : row[2].value,
            'age' : int(row[3].value),
            'est_asset_dollar' : int(row[4].value)
        })

    # corp.로 끝나는 회사명 가지고 오기 -> 스페이스로 회사명을 split하고 마지막 단위가 Corp이면 가져오기
    corp_sum = 0
    for row in data :
        if row['company'].split()[-1] == 'Corp.' :
            corp_sum = corp_sum + row['est_asset_dollar']

    return print(corp_sum)


# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 LLC로 끝나는 회사를 다니는 사람들의 자산 총 평균을 리턴합니다.
# 리턴 값의 예) 1025831.87653
def find_llc_total_asset() -> int:
    wb = openpyxl.load_workbook("/Users/eunalong/Documents/GitHub/start_de/de-course-week4/hw_data/assets.xlsx")
    ws = wb.active

    wb_flag = False
    data = []

    for row in ws :
        if not wb_flag :
            wb_flag = True
            continue
        data.append({
            'name' : row[0].value,
            'company' : row[1].value,
            'city' : row[2].value,
            'age' : int(row[3].value),
            'est_asset_dollar' : int(row[4].value)
        })

    # 평균 구하기 (sum/cnt로 구하기)
    llc_sum = 0
    llc_cnt = 0

    for row in data :
        if row['company'].split()[-1] == 'LLC' :
            llc_sum = llc_sum + row['est_asset_dollar']
            llc_cnt = llc_cnt + 1

    return print(llc_sum/llc_cnt)

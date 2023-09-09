from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.


# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 Corp.로 끝나는 회사를 다니는 사람들의 자산 총 합계를 리턴합니다.
# 리턴 값의 예) 10239102305
from openpyxl import load_workbook
def find_corp_total_asset() -> int:
    wb = load_workbook(filename='hw_data/assets.xlsx')
    first_sheet = wb.active # wb.worksheets[n]
    got_header = False
    header = None
    data = []
    hap = 0
    for r in first_sheet:
        if not got_header:
            got_header = True
            continue
        if r[1].value[-5:] == 'Corp.':
           hap += r[4].value

        data.append({
            "name": r[0].value,
            "company": r[1].value,
            "city": r[2].value,
            "age": r[3].value,
            "est_asset_dollar": r[4].value
        })

    return hap




# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xlsx 에서 LLC로 끝나는 회사를 다니는 사람들의 자산 총 평균을 리턴합니다.
# 리턴 값의 예) 1025831.87653
def find_llc_total_asset() -> int:
    wb = load_workbook(filename='hw_data/assets.xlsx')
    first_sheet = wb.active  # wb.worksheets[n]
    got_header = False
    header = None
    data = []
    hap = 0
    for r in first_sheet:
        if not got_header:
            got_header = True
            continue
        if r[1].value[-3:] == 'LLC':
            data.append(r[4].value)

    avg = sum(data)/len(data)
    return avg

def sum(list_data):
    result = 0
    for i in list_data:
    	result += i
    return result

def len(list_data):
    cnt = 0
    for i in list_data:
        cnt += 1
    return cnt


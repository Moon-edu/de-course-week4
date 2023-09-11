from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.




# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.csv파일에서 자산 평가액(est_asset_dollar)값이 가장 큰 사람의 이름과 자산 평가액의 값이 리턴되어야 합니다.
# 아래 함수를 실행하면 Tuple 값이 리턴되며, 자산 평가액이 가장 많은 사람의 이름과 자산 평가액이 리턴되어야 합니다.
# 리턴 값의 예) ("Donald", 1023014)
import csv
def find_richest_and_asset() -> Tuple:
    # 혹시 for을 한번만 사용할 수 있는 방법이 있는지 궁금합니다.
    header = None
    with open("hw_data/assets.csv", "r", encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter=',')
        got_header = False
        name=[]
        dollar=[]
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue
            name.append(row[2])
            dollar.append(dollar)

        max_name = name[0]
        max_dollar = dollar[0]
        for doll in range(len(dollar)):
            if max_dollar < dollar[doll]:
                max_name = name[doll]
                max_dollar = dollar[doll]

        return max_name, max_dollar






# 아래 함수를 실행하면, assets.csv파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 상위 3개 도시를 리턴해야 합니다.(상위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 많은 상위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_richest_city() -> list:
    header = None
    data = {}
    with open("hw_data/assets.csv", "r",encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter=',')
        got_header = False
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue

            city = row[2]
            dollar = int(row[4])

            if city in data:
                data[city][0] = data[city][0]+dollar
                data[city][1] = data[city][1] + 1
            else:
                data[city] = [dollar,1]

    for i,k in data.items():
        data[i] = k[0]/k[1]

    top3 = sorted(data.items(), key=lambda x: x[1],reverse=True)[:3]
    return [i[0] for i in top3]






from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import csv

# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.csv파일에서 자산 평가액(est_asset_dollar)값이 가장 큰 사람의 이름과 자산 평가액의 값이 리턴되어야 합니다.
# 아래 함수를 실행하면 Tuple 값이 리턴되며, 자산 평가액이 가장 많은 사람의 이름과 자산 평가액이 리턴되어야 합니다.
# 리턴 값의 예) ("Donald", 1023014)
def find_richest_and_asset() -> Tuple:
    with open("/Users/eunalong/Documents/GitHub/start_de/de-course-week4/hw_data/assets.csv","r") as csv_file :
        assets_raw = csv.reader(csv_file, delimiter=",")
        data = []
        assets = []
        header = None
        flags = False
        results = None
        for row in assets_raw :
            if not flags :
                header = row
                flags = True
            else :
                data.append(row)
                assets.append(row[4])

        for d in data :
            if d[4] == max(assets) :
                results = ((d[0], d[4]))

    return print(results)


# 아래 함수를 실행하면, assets.csv파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 상위 3개 도시를 리턴해야 합니다.(상위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 많은 상위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_richest_city() -> list:
    with open("/Users/eunalong/Documents/GitHub/start_de/de-course-week4/hw_data/assets.csv","r") as csv_file :
        assets_raw = csv.reader(csv_file, delimiter=",")
        data = []
        cities = []
        city_assets = []
        header = None
        flags = False
        for row in assets_raw :
            if not flags :
                header = row
                flags = True
            else :
                data.append(row)

        for d in data :
            if len(city_assets) == 0 :
                city_assets.append([d[2], d[4], 1])
            elif d[2] not in list(set([row[0] for row in city_assets])) :
                city_assets.append([d[2], d[4], 1])
            else :
                for row in city_assets :
                    if d[2] == row[0] :
                        row[1] = int(row[1]) + int(d[4])
                        row[2] = int(row[2]) + 1

        avgs = [[values[0], int(values[1])/int(values[2])] for values in city_assets]
        top3 = []

        while len(top3) < 3 :
            city_avgs = [values[1] for values in avgs]

            for avg in avgs :
                if max(city_avgs) == avg[1] :
                    top3.append(avg[0])
                    avgs.remove(avg)

    return print(top3)
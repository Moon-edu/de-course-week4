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
    header = None
    data = []

    with open("hw_data/assets.csv", "r") as f:

        csv_data = csv.reader(f, delimiter= ',' )  #csv.py => csv.py 원상복구

        got_header = False
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue
            data.append(row)

    data = sorted(data, key=lambda x: x[4], reverse=True)
    max_asset = data[0][0], int(data[0][4])

    return max_asset


# 아래 함수를 실행하면, assets.csv파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 상위 3개 도시를 리턴해야 합니다.(상위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 많은 상위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
import csv
def find_top3_richest_city() -> list:
    header = None
    data = []
    city_list = {}
    city_final = []
    with open("hw_data/assets.csv", "r") as f:
        csv_data = csv.reader(f, delimiter= ',')

        got_header = False
        for row in csv_data:
            if  got_header is False:
                got_header = True
                continue
            data.append(row)

        for d in data:
            city  = d[2]
            asset = int(d[4])

            if city in city_list:
                asset_sum, city_cnt, avg = city_list[city]
                city_list[city] = ((asset_sum + asset)
                                 , city_cnt  + 1
                                 , ((asset_sum + asset) / (city_cnt +1)))
            else:
                city_list[city] = (asset,  1 , (asset / 1)) #asset_sum, city_cnt, avg


    city_list = sorted(city_list.items(), key=lambda x: x[1][2], reverse = True)
    city_rank3 = city_list[0:3]


    for i in range(len(city_rank3)):
        city_final.append(city_rank3[i][0])

    return city_final


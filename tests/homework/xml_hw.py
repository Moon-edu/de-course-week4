from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import xmltodict

# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xml 자산 평가액(est_asset_dollar)값이 가장 적은 사람의 이름과 자산 평가액의 값이 리턴되어야 합니다.
# 아래 함수를 실행하면 Tuple 값이 리턴되며, 자산 평가액이 가장 적은 사람의 이름과 자산 평가액이 리턴되어야 합니다.
# 리턴 값의 예) ("Donald", -102314)
def find_poor_and_asset() -> Tuple:
    with open("hw_data/assets.xml", "r") as xml_file :
        data = xmltodict.parse(xml_file.read())['data']['asset']

        # 가장 작은 자산 평가액 도출
        asset = [int(row['est_asset_dollar']) for row in data]
        min_asset = []

        # data에서 가장 작은 평가액과 동일한 평가액을 가지고 있는 row만 추출
        for row in data :
            if int(row['est_asset_dollar']) == min(asset) :
                min_asset.append((row['name'], row['est_asset_dollar']))

    return(print(min_asset[0]))


# 아래 함수를 실행하면, assets.xml파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 하위 3개 도시를 리턴해야 합니다.(하위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 적은 하위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_poorest_city() -> list:
    with open("hw_data/assets.xml", "r") as xml_file :
        data = xmltodict.parse(xml_file.read())['data']['asset']

    # 도시 자산 평가액 평균
    city_agg = []
    city_cnt = 0
    cities = []

    for row in data :
        if row['city'] not in cities :
            city_agg.append([row['city'], int(row['est_asset_dollar']), 1])
            cities.append(row['city'])
        else :
            for agg_info in city_agg :
                if row['city'] == agg_info[0] :
                    agg_info[1] = agg_info[1] + int(row['est_asset_dollar'])
                    agg_info[2] = agg_info[2] + 1

        city_avg = [[row[0], row[1]/row[2]] for row in city_agg]

    # 자산 평균액이 bottom3 구하기
    bottom3 = []
    while len(bottom3) < 3 :
        asset_avg = [avg[1] for avg in city_avg]

        for item in city_avg :
            if item[1] == min(asset_avg) :
                bottom3.append(item[0])
                city_avg.remove(item)

    return(print(bottom3))


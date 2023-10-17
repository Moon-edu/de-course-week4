from typing import Tuple
import xmltodict

# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.


# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.xml 자산 평가액(est_asset_dollar)값이 가장 적은 사람의 이름과 자산 평가액의 값이 리턴되어야 합니다.
# 아래 함수를 실행하면 Tuple 값이 리턴되며, 자산 평가액이 가장 적은 사람의 이름과 자산 평가액이 리턴되어야 합니다.
# 리턴 값의 예) ("Donald", -102314)
def find_poor_and_asset() -> Tuple:
    data = []
    min_asset = float("inf")

    with open("hw_data/assets.xml", "r") as f:
        xml_data = xmltodict.parse(f.read())

    for d in xml_data["data"]["asset"]:
        data.append({"name": d["name"], "est_asset_dollar": d["est_asset_dollar"]})

    for d in data:
        if int(d["est_asset_dollar"]) < min_asset:
            min_asset = int(d["est_asset_dollar"])
            min_name = d["name"]

    return min_name, min_asset


# result1 = find_poor_and_asset()
# print(result1)


# 아래 함수를 실행하면, assets.xml파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 하위 3개 도시를 리턴해야 합니다.(하위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 적은 하위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_poorest_city() -> list:
    data = []
    city = dict()
    with open("hw_data/assets.xml", "r") as f:
        xml_data = xmltodict.parse(f.read())

    for d in xml_data["data"]["asset"]:
        data.append({"city": d["city"], "est_asset_dollar": d["est_asset_dollar"]})

    for d in data:
        city_name = d["city"]
        city_asset = int(d["est_asset_dollar"])

        if city_name in city:
            count, asset_sum, avg = city[city_name]
            city[city_name] = (
                count + 1,
                asset_sum + city_asset,
                ((avg * count) + city_asset) / (count + 1),
            )
        else:
            city[city_name] = (1, city_asset, city_asset)

    city = sorted(city.items(), key=lambda x: x[1][2])

    top_3_poor = [city[0][0], city[1][0], city[2][0]]

    return top_3_poor


# result2 = find_top3_poorest_city()
# print(result2)

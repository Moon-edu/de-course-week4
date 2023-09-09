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
    with open("hw_data/assets.xml", "r",encoding='utf-8') as f:
        xml_data = xmltodict.parse(f.read())

    data =[]
    #est_asset_dollar=[]
    for d in range(len(xml_data["data"]["asset"])):
        data.append([xml_data["data"]["asset"][d]["name"],int(xml_data["data"]["asset"][d]["est_asset_dollar"])])
        # company = xml_data["data"]["asset"][d]["company"]
        # city = xml_data["data"]["asset"][d]["city"]
        # age = xml_data["data"]["asset"][d]["age"]
        #est_asset_dolla = int(xml_data["data"]["asset"][d]["est_asset_dollar"]))
    min_name, min_price = [0][0], data[0][-1]
    for i in range(1, len(data)):
        if  min_price > data[i][-1]:
            min_name, min_price = data[i][0], data[i][-1]

    return min_name, int(min_price)
# 아래 함수를 실행하면, assets.xml파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 하위 3개 도시를 리턴해야 합니다.(하위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 적은 하위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_poorest_city() -> list:
    with open("hw_data/assets.xml", "r",encoding='utf-8') as f:
        xml_data = xmltodict.parse(f.read())

    data ={}
    #est_asset_dollar=[]
    for d in range(len(xml_data["data"]["asset"])):
        city = xml_data["data"]["asset"][d]["city"]
        est_asset_dolla = int(xml_data["data"]["asset"][d]["est_asset_dollar"])
        if city in data.keys():
            data[city].append(est_asset_dolla)
        else:
            data[city]= [est_asset_dolla]

    data_city = list(data.keys())
    avg_list = []
    avg_city_dic = {}
    for i in range(len(data_city)):
        avg = round(sum(data[data_city[i]]) / len(data[data_city[i]]))
        avg_city_dic[data_city[i]] = avg
        avg_list.append(avg)
    avg_city_dic=sorted(avg_city_dic.items(), key=lambda x: x[1])

    result = []
    for i in range(3):
        result.append(avg_city_dic[i][0])
    return result

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


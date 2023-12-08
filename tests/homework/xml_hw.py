from typing import Tuple
import xmltodict
import heapq

def find_poor_and_asset() -> Tuple:
    with open('hw_data/assets.xml', encoding='utf-8') as f:
        list_xml_data = xmltodict.parse(f.read())['data']['asset']

    min_est_asset_dollar_data = min(list_xml_data, key=lambda xml_data:int(xml_data['est_asset_dollar']))

    return (min_est_asset_dollar_data['name'], int(min_est_asset_dollar_data['est_asset_dollar']))

def find_top3_poorest_city() -> list:
    dict_city = {}  # key: name, value: [sum(est_asset_dollar), count]
    list_heapq = []  # 0: -sum(est_asset_dollar)/count, 1: city_name

    with open('hw_data/assets.xml', encoding='utf-8') as f:
        list_xml_data = xmltodict.parse(f.read())['data']['asset']

    for xml_data in list_xml_data:
        if xml_data['name'] in dict_city:
            dict_city[xml_data['name']][0] += int(xml_data['est_asset_dollar']) # sum(est_asset_dollar)
            dict_city[xml_data['name']][1] += 1 # count
        else:
            dict_city[xml_data['name']] = [int(xml_data['est_asset_dollar']), 1]

    for city_name, city_data in dict_city.items():
        heapq.heappush(list_heapq,((city_data[0] / city_data[1]), city_name))  # citydata(0: sum(est_asset_dollar), 1: count), list_heapq(0: sum(est_asset_dollar)/count, 1: city_name)

    return [heapq.heappop(list_heapq)[1], heapq.heappop(list_heapq)[1], heapq.heappop(list_heapq)[1]]  # list_heapq(0: sum(est_asset_dollar)/count, 1: city_name)
from typing import Tuple
import xmltodict

def find_poor_and_asset() -> Tuple:
    with open('hw_data/assets.xml', encoding='utf-8') as f:
        list_xml_data = xmltodict.parse(f.read())['data']['asset']

    min_est_asset_dollar_data = min(list_xml_data, key=lambda xml_data:xml_data['est_asset_dollar'])

    return (min_est_asset_dollar_data['name'], min_est_asset_dollar_data['est_asset_dollar'])

def find_top3_poorest_city() -> list:
    with open('hw_data/assets.xml', encoding='utf-8') as f:
        list_xml_data = xmltodict.parse(f.read())['data']['asset']

    dict_city = {}
    for xml_data in list_xml_data:
        if xml_data['name'] in dict_city:
            dict_city[xml_data['name']].append(int(xml_data['est_asset_dollar']))
        else:
            dict_city[xml_data['name']] = [int(xml_data['est_asset_dollar'])]

    return [items[0] for items in sorted(dict_city.items(), key=lambda items: sum(items[1])/len(items[1]))[:3]]
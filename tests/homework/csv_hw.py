from typing import Tuple
import csv

def find_richest_and_asset() -> Tuple:
    list_csv_data = []
    header_col = None

    with open('hw_data/assets.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header_col = dict((value, idx) for idx, value in enumerate(next(csv_reader)))

        for data in csv_reader:
            list_csv_data.append(data)

    max_csv_data = max(list_csv_data, key=lambda csv_data: csv_data[header_col['est_asset_dollar']])
    return (max_csv_data[header_col['name']], max_csv_data[header_col['est_asset_dollar']])


def find_top3_richest_city() -> list:
    list_csv_data = []
    header_col = None

    with open('hw_data/assets.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header_col = dict((value, idx) for idx, value in enumerate(next(csv_reader)))

        for data in csv_reader:
            list_csv_data.append(data)

    dict_city = {}
    for csv_data in list_csv_data:
        if csv_data[header_col['city']] in dict_city:
            dict_city[csv_data[header_col['city']]].append(int(csv_data[header_col['est_asset_dollar']]))
        else:
            dict_city[csv_data[header_col['city']]] = [int(csv_data[header_col['est_asset_dollar']])]

    return [items[0] for items in sorted(dict_city.items(), key=lambda items: sum(items[1])/len(items[1]), reverse=True)[:3]]


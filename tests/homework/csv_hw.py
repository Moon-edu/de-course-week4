from typing import Tuple
import csv
import heapq

def find_richest_and_asset() -> Tuple:
    max_csv_data = [] # [0: name, 1: est_asset_dollar]

    with open('hw_data/assets.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header_col = dict((value, idx) for idx, value in enumerate(next(csv_reader)))

        for data in csv_reader:
            if not max_csv_data:
                max_csv_data = [data[header_col['name']], int(data[header_col['est_asset_dollar']])]

            elif max_csv_data[1] < int(data[header_col['est_asset_dollar']]): # max_csv_data[0: name, 1: est_asset_dollar]
                max_csv_data = [data[header_col['name']], int(data[header_col['est_asset_dollar']])]

    return tuple(max_csv_data)

def find_top3_richest_city() -> list:
    dict_city = {} # key: city, value: [sum(est_asset_dollar), count]
    list_heapq = [] # [0: -sum(est_asset_dollar)/count, 1: city]

    with open('hw_data/assets.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header_col = dict((value, idx) for idx, value in enumerate(next(csv_reader)))

        for csv_data in csv_reader:
            if csv_data[header_col['city']] in dict_city:
                dict_city[csv_data[header_col['city']]][0] += int(csv_data[header_col['est_asset_dollar']])  # sum(est_asset_dollar)
                dict_city[csv_data[header_col['city']]][1] += 1  # count
            else:
                dict_city[csv_data[header_col['city']]] = [int(csv_data[header_col['est_asset_dollar']]), 1]

    for city_name, city_data in dict_city.items():
        heapq.heappush(list_heapq, (-(city_data[0] / city_data[1]), city_name)) # citydata[0: sum(est_asset_dollar), 1: count), list_heapq(0: -sum(est_asset_dollar)/count, 1: city]

    return [heapq.heappop(list_heapq)[1], heapq.heappop(list_heapq)[1], heapq.heappop(list_heapq)[1]] # list_heapq[0: -sum(est_asset_dollar)/count, 1: city]




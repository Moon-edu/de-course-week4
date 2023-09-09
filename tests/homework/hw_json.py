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
    with open("hw_data/assets.csv", "r",encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter=',')
        got_header = False
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue
            data.append(row)

    max_name, max_price = data[0][0], data[0][-1]
    for i in range(1,len(data)):
        if data[i][-1] > max_price:
            max_name,max_price = data[i][0], data[i][-1]

    return max_name, int(max_price)




# 아래 함수를 실행하면, assets.csv파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 상위 3개 도시를 리턴해야 합니다.(상위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 많은 상위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_richest_city() -> list:
    header = None
    city = dict()

    with open("hw_data/assets.csv", "r",encoding='utf-8') as f:
        csv_data = csv.reader(f, delimiter=',')
        got_header = False
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue

            if row[2] in city.keys():
                city[row[2]].append(int(row[-1]))
            else:
                city[row[2]] = [int(row[-1])]


        citys =list(city.keys())
        avg_list=[]
        avg_city_dic ={}
        for i in range(len(citys)):
            avg = round(sum(city[citys[i]]) / len(city[citys[i]]))
            avg_city_dic[citys[i]] = avg
            avg_list.append(avg)



        avg_city_dic=sorted(avg_city_dic.items(), key=lambda x: x[1], reverse=True)

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










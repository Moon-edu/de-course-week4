import json
from datetime import datetime

def run():

    with open("dataset/sample.json", "r") as f:
        json_data = json.load(f)

    print(f"Sample data is {json_data[0]}")

    filtered = []  # 2018 ~ 2020
    for d in json_data:
        # method1. datetime 으로 파싱하는 방법
        parsed_datetime = datetime.strptime(d["datadate"], "%Y-%m-%dT%H:%M:%SZ")  # 2018-05-10T00:15:06Z
        year = parsed_datetime.year

        # method2. 더 쉬운 방법: 날짜 포맷이 일정하므로, 첫 4자는 무조건 연도라는 점을 이용
        year_str = d["datadate"][0:4]
        year = int(year_str)

        if 2018 <= year <= 2020:
            filtered.append(d)

    # print sample
    for i in range(0, 3):
        d = filtered[i]
        print(f"""{d["first_name"]} {d["last_name"]} {d["datadate"]}""")
if __name__ == "__main__":
    run()

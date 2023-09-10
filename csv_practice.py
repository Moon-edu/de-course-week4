import csv


def run():
    import time
    start_time = time.time()  # 측정 시작
    header = None
    data = []
    with open("dataset/sample.csv", "r") as f:
        csv_data = csv.reader(f, delimiter=',')
        got_header = False
        for row in csv_data:
            if not got_header:
                header = row
                got_header = True
                continue
            data.append(row)

    male = []
    female = []
    genderqueer = []

    for d in data:
        if d[4] == "Female":
            if len(female) < 5:
                female.append(f"{d[1]} {d[2]}")
        elif d[4] == "Male":
            if len(male) < 5:
                male.append(f"{d[1]} {d[2]}")
        elif d[4] == "Genderqueer":
            if len(genderqueer) < 5:
                genderqueer.append(f"{d[1]} {d[2]}")

        if len(male) == 5 and len(female) == 5 and len(genderqueer) == 5:
            break
    print(f"Male {male}")
    print(f"Female {female}")
    print(f"Genderqueer {genderqueer}")

    # 프로그램 소스코드
    end_time = time.time()  # 측정 종료
    print("time:", end_time - start_time)  # 수행 시간 출력
if __name__ == "__main__":
    run()

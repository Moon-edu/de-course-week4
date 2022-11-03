import csv


def run():
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


if __name__ == "__main__":
    run()

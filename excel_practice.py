from openpyxl import load_workbook

def run():
    wb = load_workbook(filename='dataset/sample.xlsx')
    first_sheet = wb.active # wb.worksheets[n]
    got_header = False
    header = None
    data = []
    for r in first_sheet:
        if not got_header:
            got_header = True
            continue
        data.append({
            "name": r[1].value,
            "job": r[2].value,
            "department": r[3].value,
            "age": r[7].value,
            "salary": r[9].value
        })

    result = []
    for d in data:
        if d["age"] >= 30 and d["salary"] > 150000:
            result.append(d)

    for d in result:
        print(f"""{d["name"]} {d["salary"]}""")

if __name__ == "__main__":
    run()

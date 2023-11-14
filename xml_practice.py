import xmltodict

def run():
    with open("dataset/sample.xml", "r", encoding="utf-8") as f:
        xml_data = xmltodict.parse(f.read())
        # print(xml_data)
    data = []
    for d in xml_data["dataset"]["record"]:
        email = d["email"]
        domain = email.split("@")[1] # abc@google.cu
        if domain.startswith("google."):
            data.append(d)

    for d in data:
        print(f"""{d["first_name"]} {d["last_name"]} {d["email"]}""")

if __name__ == "__main__":
    run()

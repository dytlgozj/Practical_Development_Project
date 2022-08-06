import json


def open_json_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return json.load(file)
        except ValueError as e:
            print(f"JSON 데이터를 파싱하는 데 실패했습니다. 사유 = {e}")
            return None


json_data = open_json_file("message1.json")
if json_data:
    print(json_data)

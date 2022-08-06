import json


def open_json_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return json.load(file)
        except ValueError as e:
            print(f"JSON 데이터를 파싱하는 데 실패했습니다. 사유 = {e}")
            return None


json_data = open_json_file("message1.json")
if not json_data:
    exit(0)

num_value = json_data["number"]
float_value = json_data["pi"]
str_value = json_data["str"]
empty_value = json_data["null_key"]

print(f"num_value = {num_value}")
print(f"float_value = {float_value}")
print(f"str_value = {str_value}")
print(f"empty_value = {empty_value}")

print(f"object = {json_data['object']['object2']['number2']}")

for i in json_data["num_array"]:
    print(f"n = {i}")

# 정상적인 키가 아니거나 해커의 변조 등으로 인한 오류.
# unknown_value = json_data["unknown_key"]
# print(f"{unknown_value}")


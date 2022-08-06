import yaml


def open_yaml_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.YAMLError as e:
            print(f"Yaml 데이터를 파싱하는 데 실패했습니다. 사유 = {e}")
            return None


yaml_data = open_yaml_file("message1.yaml")
if not yaml_data:
    exit(0)

num_value = yaml_data["number"]
float_value = yaml_data["pi"]
str_value = yaml_data["str"]
empty_value = yaml_data["null_key"]

print(f"num_value = {num_value}")
print(f"float_value = {float_value}")
print(f"str_value = {str_value}")
print(f"empty_value = {empty_value}")

print(f"object = {yaml_data['object']['object2']['number2']}")

for i in yaml_data["num_array"]:
    print(f"n = {i}")

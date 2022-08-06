import yaml


def open_yaml_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.YAMLError as e:
            print(f"Yaml 데이터를 파싱하는 데 실패했습니다. 사유 = {e}")
            return None


yaml_data = open_yaml_file("realapp_config2.yaml")
if yaml_data:
    print(yaml_data)

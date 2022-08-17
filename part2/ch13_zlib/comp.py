import zlib
import json


def open_json_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return json.load(file)
        except ValueError as e:
            print(f"JSON 데이터를 파싱하는 데 실패했습니다. 사유 = {e}")
            return None


json_object = open_json_file("..\\ch08_json\\message1.json")
json_str = json.dumps(json_object, ensure_ascii=False)
json_byte_data = json_str.encode("utf8")

compressed_data = zlib.compress(json_byte_data, level=-1)
crc32 = zlib.crc32(compressed_data)

print(f"json_str 데이터 길이 = {len(json_byte_data)}")
print(f"압축된 compressed_json 데이터 길이 = {len(compressed_data)}")
print(f"압축된 compressed_json 데이터 CRC32 = {crc32}")

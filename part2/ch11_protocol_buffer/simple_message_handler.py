import simple_message_pb2
import uuid

from google.protobuf import text_format
from google.protobuf import json_format
import json


def create_new_msg():
    new_msg = simple_message_pb2.SimpleMessage()
    new_msg.name = u"문자열"
    new_msg.num64 = 12345
    new_msg.float64 = 12345.6
    new_uuid = uuid.uuid4()
    print(f"new_uuid = {new_uuid}")
    new_msg.uuid = new_uuid.bytes
    new_msg.type = simple_message_pb2.SimpleMessage.Ping
    new_msg.num64_list.append(1)
    new_msg.num64_list.append(2)
    new_msg.name_list.append(u"one")
    new_msg.name_list.append(u"two")
    new_msg.map_field["key1"] = u"value1"
    new_msg.map_field["key2"] = u"value2"
    new_msg.another_msg.name = u"문자열2"
    new_msg.another_msg.num64 = 56789

    for i in range(5):
        another_msg2 = simple_message_pb2.AnotherMessage()
        another_msg2.name = f"문자열 - {i}"
        another_msg2.num64 = i
        new_msg.another_msg2.append(another_msg2)

    return new_msg


simple_message = create_new_msg()
print("------------------------------------------------")
print(f"name = {simple_message.name}")
print(f"num64 = {simple_message.num64}")
print(f"float64 = {simple_message.float64}")
print(f"uuid = {str(uuid.UUID(bytes=simple_message.uuid))}")

index = 0
for num64 in simple_message.num64_list:
    print(f"num64_list[{index}].num64 = {num64}")
    index += 1

index = 0
for name in simple_message.name_list:
    print(f"name_list[{index}].name = {name}")
    index += 1

print(f"type = {simple_message.type}")

for key in simple_message.map_field:
    print(f"map_field[{key}] = {simple_message.map_field[key]}")

print(f"another_msg.name = {simple_message.another_msg.name}")
print(f"another_msg.num64 = {simple_message.another_msg.num64}")

index = 0
for msg2 in simple_message.another_msg2:
    print(f"another_msg2[{index}].name = {msg2.name}, num64 = {msg2.num64}")
    index += 1

print("------------------------------------------------")

# 프로토콜 버퍼는 바이너리 규격이나, utf-8, JSON 형식으로 변환하는 것은 가능하다.
text_message = text_format.MessageToString(simple_message, as_utf8=True)
print(text_message)

json_str = json_format.MessageToJson(simple_message)
print(json_str)

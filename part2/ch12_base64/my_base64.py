from bitstring import BitArray
import re


def open_json_file(filename):
    with open(filename, mode="rb") as file:
        return file.read()


# 인코딩 과정
data = open_json_file("..\\ch08_json\\message1.json")
bit_str = BitArray(data).bin
# print(bit_str)

pad_count = 0
while len(bit_str) % 24 != 0:
    bit_str += "00000000"
    pad_count += 1

b64_str = ""
b64_chs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

bit_list = re.findall(r"(\d{6})", bit_str)
if pad_count > 0:
    bit_list = bit_list[:-pad_count]

for bit in bit_list:
    v = int(bit, 2)
    b64_str += b64_chs[v]

b64_str += ("=" * pad_count)

print(f"my_base64 = {b64_str}")


# 디코딩 과정
bit_str = ""
for ch in b64_str:
    # 이 조건은 base64 문자열이 분명하다 해도 필요한데, 그 이유는 패딩문자는 디코딩하지 않아도 되기 때문이다.
    if ch in b64_chs:
        bin_ch = bin(b64_chs.index(ch)).lstrip("0b")
        bin_ch = (6 - len(bin_ch)) * "0" + bin_ch
        bit_str += bin_ch

with open("message2.json", "wb") as file:
    file.write(bytes(int(bit_str[i : i + 8], 2) for i in range(0, len(bit_str), 8)))

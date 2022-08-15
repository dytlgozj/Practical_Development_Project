import os
import struct


for i in range(10):
    random_four_byte = os.urandom(4)
    random_integer = struct.unpack("<L", random_four_byte)[0]
    print(f"hex = {random_four_byte.hex()}, integer = {str(random_integer)}")

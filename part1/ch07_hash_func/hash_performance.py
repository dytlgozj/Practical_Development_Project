import hashlib
import time


def computeMD5(str):
    hasher = hashlib.md5()
    hasher.update(str.encode("utf-8"))
    return hasher.hexdigest()


def computeSHA512(str):
    hasher = hashlib.sha512()
    hasher.update(str.encode("utf-8"))
    return hasher.hexdigest()


md5_t1 = time.monotonic()
for i in range(1000000):
    computeMD5(f"hash_test_key_{i}")
md5_t2 = time.monotonic()

sha2_t1 = time.monotonic()
for i in range(1000000):
    computeSHA512(f"hash_test_key_{i}")
sha2_t2 = time.monotonic()


print(f"Elapsed time(MD5) = {md5_t2 - md5_t1}")
print(f"Elapsed time(SHA-512) = {sha2_t2 - sha2_t1}")

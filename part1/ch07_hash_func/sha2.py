import hashlib


def computeSHA256(str):
    hasher = hashlib.sha256()
    hasher.update(str.encode("utf-8"))
    return hasher.hexdigest()


def computeSHA512(str):
    hasher = hashlib.sha512()
    hasher.update(str.encode("utf-8"))
    return hasher.hexdigest()


hash1 = computeSHA256("해시 값 1")
hash2 = computeSHA256("해시 값 2")
hash3 = computeSHA512("해시 값 1")
hash4 = computeSHA512("해시 값 2")

print(f"해시 값 1 = {hash1} / 길이 = {len(hash1)}")
print(f"해시 값 2 = {hash2} / 길이 = {len(hash2)}")
print(f"해시 값 3 = {hash3} / 길이 = {len(hash3)}")
print(f"해시 값 4 = {hash4} / 길이 = {len(hash4)}")

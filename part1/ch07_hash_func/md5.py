import hashlib


def computeMD5(str):
    hasher = hashlib.md5()
    hasher.update(str.encode("utf-8"))
    return hasher.hexdigest()


hash1 = computeMD5("해시 값 1")
hash2 = computeMD5("해시 값 2")

print(f"해시 값 1 = {hash1} / 길이 = {len(hash1)}")
print(f"해시 값 2 = {hash2} / 길이 = {len(hash2)}")

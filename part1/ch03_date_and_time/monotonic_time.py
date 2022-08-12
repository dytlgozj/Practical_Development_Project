import time


t1 = time.monotonic()

while True:
    t2 = time.monotonic()
    if t2 >= t1 + 3:
        break

    time.sleep(0.1)

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"diff = {t2 - t1}")

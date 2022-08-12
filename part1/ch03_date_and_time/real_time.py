import datetime
import time


t1 = datetime.datetime(year=2022, month=8, day=11, hour=16, minute=25, second=00)

while True:
    now = datetime.datetime.now()
    print(f"현재 시간 : {now}")
    print(f"루프 만료 시간 : {t1}")
    if t1 <= now:
        break
    time.sleep(1)

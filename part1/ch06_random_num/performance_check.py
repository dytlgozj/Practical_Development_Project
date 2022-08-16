import random
import time
import os


random.seed()
prng_t1 = time.monotonic()
for i in range(1000000):
    random.random()

prng_t2 = time.monotonic()

srng_t1 = time.monotonic()
for i in range(1000000):
    random_four_byte = os.urandom(4)

srng_t2 = time.monotonic()

print(f"Elapsed time(PRNG) = {prng_t2 - prng_t1}")
print(f"Elapsed time(SRNG) = {srng_t2 - srng_t1}")

import random
import time
a = 0
N = 275
start_time = time.time()

i = N
while i > 0:
   a = a + random.randint(1, 101)
   i = i // 2

stop_time = time.time()
print("stop_time = ", stop_time)
print("diff_time = ", (stop_time - start_time), " seconds.")

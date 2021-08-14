import random
import time
a = 0
N = 64
start_time = time.time()

i = 0
while i < N:
   j = 1
   while j < N:
       a = a + random.randint(1, 101)
       print(i, j, a)
       j = j * 2
   i = i + 1

print(a)
stop_time = time.time()
print("stop_time = ", stop_time)
print("diff_time = ", (stop_time - start_time), " seconds.")
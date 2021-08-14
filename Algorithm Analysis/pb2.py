import random
import time
a = 0
N = 80
start_time = time.time()
print("start time = ", start_time)

for i in range(N):
   for j in range(N):
       a = a + random.randint(1, 101)
 
print(a)
stop_time = time.time()
print("stop_time = ", stop_time)
print("diff_time = ", (stop_time - start_time), " seconds.")

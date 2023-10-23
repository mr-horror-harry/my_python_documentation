import time

t1 = time.time()
for i in range(100000000):
    pass
t2 = time.time()

print("Time taken:",t2-t1,"secs")

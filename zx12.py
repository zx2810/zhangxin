import time
 
time_begin = time.time()
t=0
for i in range(10):
    t+=55555**55555*i
end = time.time()
time = end - time_begin
 
print('time:', time)

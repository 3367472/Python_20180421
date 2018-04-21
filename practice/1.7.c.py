import time

print time.localtime()
print time.time()
print time.strftime("%M", time.localtime())
time = int(time.strftime("%M", time.localtime()))
if time % 60 == 0:
    print 'On the hour!'

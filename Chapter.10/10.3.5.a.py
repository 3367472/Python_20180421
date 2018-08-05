# encoding: utf-8
import time

print(time.asctime())
print(time.strptime(time.asctime()))
time.sleep(1)
print(time.localtime())
print(time.mktime(time.localtime()))
print(time.time())
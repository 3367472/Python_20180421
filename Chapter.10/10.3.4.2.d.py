# encoding: utf-8
from heapq import *
from random import shuffle

data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print(heap)
print(heapreplace(heap, 0.5))
print(heap)
print(heapreplace(heap, 10))
print(heap)

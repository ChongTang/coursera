'''
Treat the input as a stream of integer, calculate the Median at realtime.
Compute the sum of those Medians mod 10000.
'''
import heapq


min_heap = []
max_heap = []
res = 0
with open('Median.txt') as f:
    for line in f:
        val = int(line)
        if not max_heap or val < -max_heap[0]:
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
        if len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        res += -max_heap[0]

print(res % 10000)

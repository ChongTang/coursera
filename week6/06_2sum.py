'''
Compute the number of target values t in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,y in the input file that satisfy x+y=t
'''
import bisect


arr = None
with open('algo1-programming_prob-2sum.txt') as f:
    arr = list(map(int, f.readlines()))

arr.sort()
vis = [0] * 20001

for i, val in enumerate(arr):
    l = bisect.bisect_left(arr, -10000-val, i + 1)
    r = bisect.bisect_right(arr, 10000-val, i + 1)
    for j in range(l, r):
        vis[val + arr[j] + 10000] = 1
print(sum(vis))

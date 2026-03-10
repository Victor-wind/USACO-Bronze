# All tests pass within 1800 ms

import sys
from collections import Counter
import heapq

def solution(N, K, elements):
    steps = 0
    # print(N,K)
    counts = Counter(elements)    
    heap = []    
    for k in counts.keys():
        if K > 0:
            heapq.heappush(heap, k)
        else:
            heapq.heappush(heap, -k)
    # print(f'{counts=} {heap=}')
    while heap:
        smallest = heapq.heappop(heap)
        # print(f'debug {smallest=}')
        if K < 0: smallest = -smallest
        new_key = smallest + K
        val = counts[smallest]
        # print(f'{smallest=} {val=} {new_key=}')
        # if smallest > 40 or smallest < -40: break
        if val > 1: # need to move (val-1) elements to new positions
            steps += (val - 1)
            if new_key not in counts:
                index_to_push = new_key if K >0 else -new_key
                # print(f'debug heappush {new_key=} {index_to_push=}')
                heapq.heappush(heap, index_to_push)
            counts[new_key] += (val - 1)
    print(steps)
        
    
    
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    elements = [int(x) for x in sys.stdin.readline().strip().split()]
    solution(N, K, elements)

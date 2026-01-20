# Test cases [13 - 18] time out

import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
grid = [[0] * (N+1) for _ in range(N+1)]
val_sum = [[0] * (N+1) for _ in range(N+1)] # the summary of values in KxK photo: topleft at (i,j)
Q = int(sys.stdin.readline().strip())
result = list()


def cal_beauty(r, c, v):
    max_total = 0
    row_low = max(r - K + 1, 0)
    row_high = min(r+1, N-K+1+1)
    col_low = max(c - K + 1, 0)
    cow_high = min(c+1, N-K+1+1)
    # print("debug:", row_low, row_high, col_low, cow_high)
    # loop through all photos which include (r,c)
    max_total = 0
    diff = v - grid[r][c]
    for y in range(row_low, row_high):
        for x in range(col_low, cow_high):
            # don't re-calculate the K*K photo grid, use val_sum instead
            val_sum[y][x] += diff
            max_total = max(max_total, val_sum[y][x])
            ''' 
            total = 0
            for i in range(K):
                for j in range(K):
                    total += grid[y+i][x+j]
            max_total = max(max_total, total)
            '''
    grid[r][c] = v
    if not result or (max_total >= result[-1]):
        result.append(max_total)
    else:
        result.append(result[-1])


for _ in range(Q):
   r, c, v = [int(x) for x in sys.stdin.readline().split()]
   cal_beauty(r,c, v)

out = '\n'.join(map(str, result))
sys.stdout.write(out)

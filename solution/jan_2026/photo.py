import sys

N, K = [int(x) for x in sys.stdin.readline().split()]
grid = [ [0] * (N+1) for _ in range(N+1)]
Q = int(sys.stdin.readline().strip())
result = list()

def cal_beauty(r,c):
    max_total = 0
    row_low = max(r - K + 1, 0)
    row_high = min(r+K, N-K+1)
    col_low = max(c - K + 1, 0)
    cow_high = min(c+K, N-K+1)
    for y in range(row_low, row_high):
        for x in range(col_low, cow_high):
            total = 0
            for i in range(K):
                for j in range(K):
                    total += grid[y+i][x+j]
            max_total = max(max_total, total)
    if (result and max_total >= result[-1]) or not result:
        result.append(max_total)
    else:
        result.append(result[-1])
    
for _ in range(Q):
   r,c,v = [int(x) for x in sys.stdin.readline().split()]
   print(r,c,v)
   grid[r][c] = v
   cal_beauty(r,c)

for b in result:
    print(b)
    

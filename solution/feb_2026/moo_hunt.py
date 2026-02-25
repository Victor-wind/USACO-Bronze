# test cases 9-12 time out

import sys

N, K = [int(x) for x in sys.stdin.readline().split()]

# 'M' may not be the first index, like 'OMO'
cells_pos = [ [ [ 0 for _ in range(N)] for _ in range(N)] for _ in range(N)]

for _ in range(K):
    # cells_pos[x][y][z]: y<Z but x is not related with y or z
    x, y, z = [int(i)-1 for i in sys.stdin.readline().split()]
    cells_pos[x][min(y,z)][max(y,z)] += 1

scores = [ 0 for i in range(1<<N)]

for mask in range(1,1<<N):
    # mask's bits map represents s board
    msb = mask.bit_length() - 1
    # mask ^ (1 << msb) is a number removing the MSB bit
    scores[mask] = scores[mask ^ (1 << msb)]
    # addtional scores by turning msb from 0/'O' to 1/'M'
    for i in range(N):
        if (mask & 1<<i): # if i == 1/'M', skip
            continue
        for j in range(i+1, N):
            if not (mask & 1<<j):
                scores[mask] += cells_pos[msb][i][j]
    # scores also could be reduced by turning msb from 0/'O' to 1/'M'
    for m in range(msb):
        if not (mask & 1<<m): # if m == 0/'O', skip
            continue        
        for i in range(msb-1, N):
            if not (mask & 1<<i):
                scores[mask] -= cells_pos[m][msb][i]
        for j in range(msb):
            if not (mask & 1<<j):
                scores[mask] -= cells_pos[m][j][msb]
    
best_score = max(scores)
cnt = scores.count(best_score)
print(best_score, cnt)

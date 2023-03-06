import sys

# T test cases
T = int(input())
#print(f'{T=}')

def rotate(k, stamp, stamp2):
    for i in range(k):
        for j in range(k):
            stamp2[j][k-1-i] = stamp[i][j]
            
def update_stamp(i, j, k, stamp, canvas, result):
    applied = True
    for x in range(k):
        if not applied: break
        for y in range(k):
            if stamp[x][y] == '*' and canvas[i+x][j+y] == '.':
                applied = False
                break
    if not applied:
        return

    for x in range(k):
        for y in range(k):
            if stamp[x][y] == '*':
                result[i+x][j+y] = '*'
    return
    

for _ in range(T):
    input()
    N = int(input())
    canvas = list()
    for i in range(N):
        canvas.append(input())
    K = int(input())
    stamp = list()
    for i in range(K):
        stamp.append(input())
    '''
    print(f' ')
    print(f'{N=}')
    print(f'{canvas=}')
    print(f'{K=}')
    print(f'{stamp=}')
    '''
    # generate addtional rotated stamps
    stamp_1 = [ [''] * K for _ in range(K)]
    stamp_2 = [ [''] * K for _ in range(K)]
    stamp_3 = [ [''] * K for _ in range(K)]

    rotate(K, stamp, stamp_1)
    rotate(K, stamp_1, stamp_2)
    rotate(K, stamp_2, stamp_3)

    canvas_res = [ ['.'] * N for _ in range(N)]
    for i in range(N-K+1):
        for j in range(N-K+1):
            update_stamp(i,j,K,stamp,canvas,canvas_res)
            update_stamp(i,j,K,stamp_1,canvas,canvas_res)
            update_stamp(i,j,K,stamp_2,canvas,canvas_res)
            update_stamp(i,j,K,stamp_3,canvas,canvas_res)
            
    # check whether canvas == canvas_res
    possible = True
    for i in range(N):
        if not possible: break
        for j in range(N):
            if canvas[i][j] != canvas_res[i][j]:
                possible = False
    output = 'YES' if possible else 'NO'
    print(output) 
 

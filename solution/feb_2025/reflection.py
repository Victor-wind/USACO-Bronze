N, U = [int(x) for x in input().split()]
canvas = []
cells = list()
for _ in range(N):
    canvas.append(list(input().strip()))
for _ in range(U):
    r,c = [int(x) for x in input().split()]
    cells.append((r,c))

'''
for i in range(N): print(canvas[i])
for cell in cells: print(cell)
print(f'{N=} {U=}')
'''
N = N//2

def cal_op(i,j):
    # 3 reflection cells for cell (i, j)
    x1 = i
    y1 = 2*N-1-j
    x2 = 2*N-1-i
    y2 = j
    x3 = 2*N-1-i
    y3 = 2*N-1-j
    # print(i,j,x1,y1,x2,y2,x3,y3)
    chars_group = [canvas[i][j], canvas[x1][y1], canvas[x2][y2], canvas[x3][y3]]
    cnt = chars_group.count('#')    
    if cnt == 1 or cnt == 3:
        return 1
    elif cnt == 2:
        return 2
    return 0
    
def toggle_cell(i, j):
    if canvas[i][j] == '#':
        canvas[i][j] = '.'
    else:
        canvas[i][j] = '#'
        

op_needed = 0
for i in range(N):
    for j in range(N):
        op_needed += cal_op(i,j)

print(op_needed)
for cell in cells:
    i = cell[0]-1
    j = cell[1]-1
    cnt = cal_op(i,j)
    op_needed -= cnt
    toggle_cell(i,j)
    cnt = cal_op(i,j)
    op_needed += cnt
    print(op_needed)

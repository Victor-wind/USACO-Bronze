N,Q = [int(i) for i in input().split()]
configs = 0

x_y = [ [0]*N for i in range(N)]
x_z = [ [0]*N for i in range(N)]
y_z = [ [0]*N for i in range(N)]

def check_config(x, y, z):
    cnt = 0
    x_y[x][y] += 1
    if x_y[x][y] == N: cnt+=1
    
    x_z[x][z] += 1
    if x_z[x][z] == N: cnt+=1

    y_z[y][z] += 1
    if y_z[y][z] == N: cnt+=1
    
    return cnt

# if using 3D lists cube[x][y][z], tests will time out.
# so take advantage of the observation, no block (x,y,z) is the same.
# use 2D list to track how many blocks on each row/column are removed,
# if the number reaches N, there is 1*1*N block brick for that row/column.  
for _ in range(Q):
    x,y,z = [int(i) for i in input().split()]
    configs += check_config(x, y, z)
    print(configs)
 

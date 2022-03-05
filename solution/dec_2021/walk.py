T = int(input())

cnt = 0

# this dfs search overtime in test case 6 ~ 10
def find_paths(farms, N, turn_limit, turns, x, y, path):
    global cnt
   
    if x > N or y > N: # out of farm boundary
        return
    if turns > turn_limit: # too many turns
        return
    if farms[x][y] == 'H':
        return

    if x == N and y == N: # reach the destination
        #print(path, ' ',turn_limit,' ',turns )
        cnt += 1

    #move down
    d_turn = turns    
    if path and path == 'R': d_turn += 1
    find_paths(farms, N, K, d_turn, x, y+1, 'D')
    
    #move right
    d_turn = turns
    if path and path == 'D': d_turn += 1
    find_paths(farms, N, K, d_turn, x+1, y, 'R')
     

for i in range(T):
    N, K = input().split()
    N= int(N)
    K= int(K)
    farms = []
    for j in range(N):
        farms.append(input())
    #print(farms)
    cnt = 0
    find_paths(farms, N-1, K, 0, 0, 0, '')
    print(cnt)
    


T= int(input())

def move_down(path_dic, K):
    d = {}
    #print('move_down',path_dic)
    for key, v in path_dic.items():
        if key[0] == 'D':
             if key in d:  v = v+d[key] 
             d.update({key:v})
        if key[0] == 'R' and key[1] < K:
             new_key = ('D', key[1]+1)
             if new_key in d: v = v+d[new_key]
             d.update({new_key:v})
    return d

def move_right(path_dic, K):
    d = {}
    for key, v in path_dic.items():
        if key[0] == 'R':
             if key in d:  v = v+d[key]
             d.update({key:v})
        if key[0] == 'D' and key[1] < K:
             new_key = ('R', key[1]+1)
             if new_key in d: v = v+d[new_key]
             d.update({new_key:v})
    return d

def merge_path(path1, path2):
    new_path = {}
    for p1_k, p1_v in path1.items():
        if p1_k not in path2:            
            new_path.update({p1_k:p1_v})
        if p1_k in path2:
            new_path.update({p1_k:p1_v+path2[p1_k]})
    for p2_k, p2_v in path2.items():
        if p2_k not in path1:
            new_path.update({p2_k: p2_v})
            
    return new_path
            

def find_paths(pastures, N, K):
    dp = [[0] * N for i in range(N)]
    
    for i in range(1,N):
        dp[0][i] = {('R', 0):1}
        dp[i][0] = {('D', 0):1}

    k = N
    for i in range(N):
        if pastures[i][0] == 'H':
            dp[i][0] = {}; k = i; break
    for j in range(k, N):
        dp[j][0] = {}

    k = N
    for i in range(N):
        if pastures[0][i] == 'H':
            dp[0][i] = {}; k = i; break
    for j in range(k, N):
        dp[0][j] = {}

    # print(dp)
    
    for i in range(1,N):
        for j in range(1,N):
            if pastures[i][j] == 'H':
                dp[i][j] = {}
                continue
            
            #dp[i][j] comes from dp[i][j-1] and dp[i-1][j]
            # move down  from dp[i][j-1]
            d_down  = move_down(dp[i-1][j], K)
            # move right from dp[i-1][j]
            d_right = move_right(dp[i][j-1], K)
            dp[i][j] = merge_path(d_down, d_right)
            
    cnt = 0
    for v in dp[N-1][N-1].values():
        cnt += v
        
    return cnt

'''
pastures = ['...H','.H..','....', 'H...']
print(find_paths(pastures,4,3))

'''

for i in range(T):
    N,K = input().split()
    N = int(N); K = int(K)
    pastures = []
    for j in range(N):
        s = input()
        pastures.append(s)
    cnt = find_paths(pastures, N, K)
    print(cnt)


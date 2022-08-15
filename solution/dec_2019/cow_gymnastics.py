
with open('gymnastics.in') as f:
    lines = f.readlines()
    

K, N = lines[0].split()

K = int(K)
N = int(N)

# print(K, N)

    
def print_dic(d):
    for k,v in pos_dic.items():
        print("k=",k, " v=",v)
        
    
pos_dic = {}
for i in range(1, N+1):
    for j in range(1, N+1):
        key = (str(i),str(j))
        pos_dic[key] = None
        
for i in range(1,K+1):
    s = lines[i].split()
    for k in range(N):
        for t in range(k+1, N):
            key_1 = (s[k],s[t])
            
            if pos_dic[key_1] is None:                
                pos_dic[key_1] = 1
            
            key_2 = (s[t],s[k])
            pos_dic[key_2] = 0


cnt = 0
for k,v in pos_dic.items():
    if v == 1:
        cnt += 1

with open('gymnastics.out', 'w') as f:
    f.write(str(cnt))

'''
f = open('gymnastics.in')
lines = f.readlines()
lines[0] =lines[0].split()
K = int(lines[0][0])
N = int(lines[0][1])
nums_input = [i.split() for i in lines[1:]]
nums = list()
for x in nums_input:
    y = [int(i) for i in x]
    nums.append(y)

cnt = 0
def check_order(sessions, k, i, j):
    pairs = 0
    for session in sessions:
        for x in range(len(session)):
            if session[x]==i:
                i_index=x
            if session[x]==j:
                j_index=x
        if i_index < j_index:
            pairs += 1
    return pairs

for i in range(1, N+1):
    for j in range(1, N+1):        
        pairs = check_order(nums, K, i, j)
        if pairs==K:
            cnt+=1

f = open('gymnastics.out','w')
f.write(str(cnt))
'''

# contributed by lazy panda.

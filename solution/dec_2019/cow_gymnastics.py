def get_pairs(cows: list):
    n = len(cows)
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            pair = (cows[j],cows[i])
            pairs.add(pair)        
    return pairs 

with open('gymnastics.in') as f:
    lines = f.readlines()

K, N = [ int(x) for x in lines[0].split()]

cows_lst = list()
for i in range(K):
    cows = [ int(x) for x in lines[i+1].split()]
    cows_lst.append(cows)
    
#print(cows_lst)
pairs_result = get_pairs(cows_lst[0])
#print(pairs_result)
for cows in cows_lst:
    pairs = get_pairs(cows)
    pairs_result = pairs_result & pairs

print(pairs_result)
result = len(pairs_result)
with open('gymnastics.out','w') as f:
    f.write(f'{result}')


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

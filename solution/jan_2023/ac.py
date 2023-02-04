
in_list = [int(i) for i in input().split()]
N, M = in_list[0], in_list[1]

cows = list()
for i in range(N):
    t = [int(i) for i in input().split()]
    cows.append(t)

#print(f'{cows=}')

ac = list()
for i in range(M):
    t = [int(i) for i in input().split()]
    ac.append(t)

#print(f'{ac=}')

def apply_ac(k: int):
    stalls = [0]*101
    s = "{0:010b}".format(k)
    s = s[::-1]
    #print(f'{s=}')
    cost = 0
    for i in range(10):
        if s[i] == '1': # ac i is On,
            cost += ac[i][3]
            for j in range(ac[i][0], ac[i][1]+1):
                stalls[j] += ac[i][2]            

    #print(f'{stalls=} {cost=}')
    # check whether stalls satisfy requirement
    for i in range(N):
        # for cow i
        #print(f'{cows[i]=}')
        for j in range(cows[i][0], cows[i][1]+1):
            #print(f' debug {j=} {stalls[j]} {cows[i][1]}')
            if stalls[j] < cows[i][2]:
                return 10001

    return cost

x = pow(2, M)
min_cost = 10001
for i in range(x):
    cost = apply_ac(i)
    if cost != 10001:
        min_cost = min(min_cost, cost)

print(f'{min_cost}')

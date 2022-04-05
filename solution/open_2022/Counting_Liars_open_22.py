
n = int(input())
G_list = []
L_list = []
for i in range(n):
    temp_list = input().split()
    G_list.append(int(temp_list[1])) if temp_list[0] == 'G' else L_list.append(int(temp_list[1]))
    

'''
G_list = [1, 8, 10]
L_list = [2,3,4,5]

#G_list = [3]
#L_list = [2]
'''

G_list.sort()
L_list.sort()


pos = G_list+L_list
pos.append(G_list[-1]+1)
pos.append(L_list[0]-1)

min_liars = len(pos)

for p in pos:
    #print('in loop p=', p)
    cur = 0
    for g in G_list:
        if p < g: cur += 1
    for l in L_list:
        if p > l: cur += 1
        
    #print('2 in loop cur=', cur)
    min_liars = min(min_liars, cur)

print(min_liars)


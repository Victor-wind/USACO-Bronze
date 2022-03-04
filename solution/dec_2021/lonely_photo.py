import timeit
import random
from timeit import default_timer as timer


N = int(input())
cows = input()

cows_num = [1] * N

for i in range(N):
    if cows[i] == 'G':
        cows_num[i] = 0 

s1= timer()
cnt =0
i = 0
k = 0
g_cnt = 0
h_cnt = 0
break_flag = False
same_cnt = 0
for i in range(N-2):
    # optimization : do not need to restart from i/i+1, start from
    # j, as [i,j] has only 1 G or 1 H

    if i > 0 and break_flag and cows_num[j] == cows_num[i-1]:
        #print('break loop g_cnt+h_cnt=', g_cnt+h_cnt)
        if cows_num[j] == 0:
            g_cnt -= 2
        else:
            h_cnt -= 2

    else:
        k = i
        g_cnt = 0
        h_cnt = 0

    break_flag = False
    for j in range(k, N):
        if cows_num[j] == cows_num[i]:
            same_cnt += 1
        if cows_num[j] == 0:
            g_cnt += 1
        else:
            h_cnt += 1
        if (g_cnt+h_cnt)>=3 and (g_cnt == 1 or h_cnt == 1):
            cnt += 1  
        if g_cnt >= 2 and h_cnt >= 2:
            k = j
            break_flag = True            
            break   

e1 = timer()
# print(e1-s1)
print(cnt)


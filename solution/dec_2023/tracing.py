import math

N = int(input())
cows = [int(x) for x in input()]

#print(f"{N=} {cows=}")
groups = list()
cnt = 0
for i in cows:
    if i == 1:
        cnt+=1
    else:
        if cnt > 0:  groups.append(cnt)
        cnt = 0
if cnt > 0:  groups.append(cnt)

# calculate the min of max windows (days) each group of infected cows
# for (2K+1) continual infected cows, the max days is K starting from 1 cow in the middle.
# for 2K continual infected cows, the max days is K-1 starting from 2 cows in middle.
# so the max days is (X-1)//2
# if the K infected cows start from the beginning or end, the max days is K-1
min_days = N
for i,v in enumerate(groups):
    days = (v-1)//2
    if (i == 0 and cows[0] == 1) or (i == len(groups)-1 and cows[-1] == 1):
        days = v-1
    min_days = min(min_days,days)
win = 1+2*min_days
#print(f'{min_days=} {win=}')
#print(groups)

# for each group, how many infected cows are needed, so that after k days, the total # becomes groups[i]?
# if starting with 1 middle infected cow,  after k days, the total is 1+2k
# if starting with 2 middle infected cows, after k days, the total is 2+2k
# to make the # initial cows small, always start with 1 middle infected cow.
# need [groups[i]/(1+2k)] infected cow, so that after k days, the total # becomes groups[i]
cnt = 0
for x in groups:
    y = math.ceil(x/win)
    cnt += y
    #print(y)
print(cnt)

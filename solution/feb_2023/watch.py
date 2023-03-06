import sys

N, K = [int(x) for x in input().split()]
#print(N, K)

schedule = [int(x) for x in input().split()]
#print(schedule)

amont = 1+K
for i in range(1, N):
    between = schedule[i] - schedule[i-1]
    # Is extending current subscription less than a new subscription ?
    if between <= K:
        amont += between
    else:
        amont += 1+K
        
print(amont)   

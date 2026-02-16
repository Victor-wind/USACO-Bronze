import sys

N, Q = [int(x) for x in sys.stdin.readline().split()]
#print(T, k)

costs = [int(x) for x in sys.stdin.readline().strip().split()]

queries = [ int(sys.stdin.readline().strip()) for i in range(Q)]

num_lst = [ pow(2, i) for i in range(40)]

# update costs: if cost[i] > cost[i-1]*2: it is cheaper to buy 2 num_lst[i-1] than num_lst[i]
# ensure the current deal is better than previous deals
for i in range(1, N):
    x = costs[i-1]*2
    if costs[i] > x:
       costs[i] = x 

# does not need the following update to pass the official tests.
# however, for edge case cost[9999] = 1, it only cost 1 moonies for any query, the official solution has trouble
if N >= 31:
    costs[30] = min(costs[30:])

def min_cost(query):
    moonies = 0
    # num_lst[30] 2^30 > 10^9
    largest_idx = min(30, N-1)    
    # process the last possible deal: it is always the best deal  
    if query >= num_lst[largest_idx]:
        k = query//num_lst[largest_idx]
        moonies += (costs[largest_idx]*k)
        query -= (num_lst[largest_idx]*k)
    min_moonies = moonies + costs[largest_idx]
    # any query can be combined by 1,2,4,8 ... (2^k)
    for i in range(largest_idx-1, -1, -1):
        min_moonies = min(min_moonies, (costs[i+1]+moonies)) # it may be cheaper to buy more
        if query >= num_lst[i]:
            moonies += costs[i]
            query -= num_lst[i]    
    # print(f'{query=} {largest_idx=} {results=}')
    return min(min_moonies, moonies)
    
for i in range(Q):
    x = min_cost(queries[i])
    print(x)


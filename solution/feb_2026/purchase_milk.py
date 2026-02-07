import sys

N, Q = [int(x) for x in sys.stdin.readline().split()]
#print(T, k)

costs = [int(x) for x in sys.stdin.readline().strip().split()]

queries = [ int(sys.stdin.readline().strip()) for i in range(Q)]

num_lst = [ pow(2, i) for i in range(40)]

# update costs: if cost[i] > cost[i-1]*2: it is cheaper to buy 2 num_lst[i-1] than num_lst[i]
for i in range(1, N):
    x = costs[i-1]*2
    if costs[i] > x:
       costs[i] = x 

# does not need the following update to pass the tests.
# however, for corner case cost[9999] = 1, it only cost 1 moonies for any query
if N > 39:
    smallest_cost_possible = min(costs[40:])
    costs[39] = min(costs[39], smallest_cost_possible)
    

def min_cost(query):
    results = list()    
    moonies = 0
    # num_lst[39] > 10^9
    largest_idx = min(40-1, N-1)
     
    if query > num_lst[largest_idx]:
        k = query//num_lst[largest_idx]
        moonies += (costs[largest_idx]*k)
        query -= (num_lst[largest_idx]*k)
    # any query can be combined by 1,2,4,8 ... (2^k)
    for i in range(largest_idx, -1, -1):
        if query < num_lst[i]: # it may be cheaper to buy more
            results.append(costs[i]+moonies)
        else:
            moonies += costs[i]
            query -= num_lst[i]
    results.append(moonies)
    # print(f'{query=} {largest_idx=} {results=}')
    return min(results)
    
for i in range(Q):
    x = min_cost(queries[i])
    print(x)


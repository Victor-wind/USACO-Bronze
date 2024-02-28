N, M = [int(x) for x in input().split()]
direction = input()
bucket_capacities = [int(x) for x in input().split()]
in_degree = [0]*N
total_milk = sum(bucket_capacities)
for i, c in enumerate(direction):
    if c == 'L':
        j = N-1 if i == 0 else i-1         
    else:
        j = 0 if i == N-1 else i+1
    in_degree[j] +=1        
    
#print(f'{in_degree=}')
'''
follow the direction, we can build a graph. vertex is the cow, edge is the direction.
for cows (vertex) in a cycle, there is no milk overflow.
for cows not in a cycle, one unit of milk overflows at vertex entering the cycle every minute.
for example, 1->2->3->4>3. 3 and 4 is a cycle. 1->2->3 enters the cycle at 3. each has capacity 2.
At minute 1: vertex 1 has 1 unit milk; overflow at vertex 3; Other vertex has milk 2 units.
At minute 2: vertex 1 has 0 unit milk; overflow at vertex 3; Other vertex has milk 2 units.
At minute 3: vertex 1 has 0 unit milk; vertex 2 has 1 unit milk;overflow at vertex 3; Other vertex has milk 2 units.
At minute 4: vertex 1 has 0 unit milk; vertex 2 has 0 unit milk;overflow at vertex 3; Other vertex has milk 2 units.
At minute 5: vertex 1 has 0 unit milk; vertex 2 has 0 unit milk;no overflow; Other vertex has milk 2 units.
...
At minute N: vertex 1 has 0 unit milk; vertex 2 has 0 unit milk;no overflow; Other vertex has milk 2 units.

cycle detection: start at vertex k (in_degree[k] == 0), along the direction, enter a cycle where in_degree[k] > 1
there are other ways to detect a cycle in a graph, because the edges go either left or right,
the above is the simplest way. 
'''
start_cows = { i: 0 for i in range(N) if in_degree[i] == 0 }
for k in start_cows.keys():
    cow = k
    milk = 0
    while in_degree[cow] < 2:
        milk += bucket_capacities[cow]
        if direction[cow] == 'L':
            cow = N-1 if cow == 0 else cow-1
        else:
            cow = 0 if cow == N-1 else cow+1
    start_cows[k] = milk
    
#print(f'{start_cows=}')

total_lost = 0
for milk in start_cows.values():
    total_lost +=  M if milk >= M else milk

print(total_milk-total_lost)

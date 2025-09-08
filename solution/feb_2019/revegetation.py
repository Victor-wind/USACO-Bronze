with open('revegetate.in') as f:
    lines = f.readlines()

N, M = [int(x) for x in lines[0].split()]

print(N, M)
pastures_map = [set() for _ in range(N+1)]
for i in range(M):
    x, y = [int(x) for x in lines[i+1].split()]
    print(x,y)
    pastures_map[x].add(y)
    pastures_map[y].add(x)

print(pastures_map)
grass = [-1]*(N+1) # grass assigned to each pasture 

# It is the famous '4-color' math problem to color the map
for i in range(1,N+1):
    # find the grass of pasture_i's neighbor 
    used_color = [grass[k] for k in pastures_map[i] if grass[k] != -1]
    for j in range(1, 5, 1):
        # j is the color for pasture_i, it is guaranteed the color exists 
        if j not in used_color:
            grass[i] = j
            break        

print(grass)
result = ''.join([str(i) for i in grass[1::]])
print(result)
with open('revegetate.out','w') as f:
    f.write(f'{result}')

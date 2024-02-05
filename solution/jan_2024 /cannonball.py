N,S = [int(x) for x in input().split()]
pos = list()
visited = set()

# add a dummy location [9,-1], so the locations start with index 1 based. 
pos.append([9,-1])
for _ in range(N):
    pos.append([int(x) for x in input().split()])
#print(f'{N=} {S=}')
#print(f'{pos=} ')

p, direction = S, 1
broken_cnt, power = 0, 1

while True:    
    if p > N or p < 1:
        break

    # detect infinite loops: if a location is visited with the same power and direction,
    # it is a infinite loops 
    if (p,power,direction) in visited:
        break
    visited.add((p,power,direction))
    
    if pos[p][0] == 1 and power >= pos[p][1]:
        broken_cnt += 1
        pos[p][0] = -1
    if pos[p][0] == 0:
        direction *= -1
        power += pos[p][1]
    p += power*direction 
        
print(broken_cnt)      
  

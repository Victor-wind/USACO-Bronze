def toggle(pos, m, n):
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if pos[i][j] == 1:
                pos[i][j] = 0
            else:
                pos[i][j] = 1
                
    
with open('cowtip.in') as f:
    lines = f.readlines()

N = int(lines[0])
pos = list()

for i in range(1, N+1):
    pos.append([ int(x) for x in list(lines[i][0:N])])
    
print(pos)

count = 0

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if pos[i][j] == 1:
            toggle(pos, i, j)
            count += 1
            
print(pos)
print(count)

with open('cowtip.out','w') as f:
     f.write(f'{count}\n')
     

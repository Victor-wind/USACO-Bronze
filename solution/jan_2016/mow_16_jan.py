with open('mowing.in') as f:
    lines = f.readlines()

N= int(lines[0])

lines = [line.split() for line in lines]

for i in range(1, 1+N):
   lines[i][1] = int(lines[i][1])

print(lines)

x, y = 0,0
delta_x, delta_y = 0,0
t = 0
cells = dict()
min_x = 1001
for i in range(1, 1+N):
   if lines[i][0] == 'N':
      delta_x, delta_y = 0,1
   if lines[i][0] == 'S':
      delta_x, delta_y = 0,-1
   if lines[i][0] == 'E':
      delta_x, delta_y = 1,0
   if lines[i][0] == 'W':
      delta_x, delta_y = -1,0
   n = lines[i][1]
   for i in range(n):
      x += delta_x
      y += delta_y
      t += 1
      if (x, y) in cells:
         #print(f' alreay mowed cell {x},{y}')
         min_x = min(min_x, t-cells[(x, y)])
      cells[(x, y)] = t
      #print(f'mowed cell {x},{y} = {t}')
   
print(min_x)
if min_x == 1001:
   min_x = -1
   
with open('mowing.out','w') as f:
    f.write(f'{min_x}\n')
    
   

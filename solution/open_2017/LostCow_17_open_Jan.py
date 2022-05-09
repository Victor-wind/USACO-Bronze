with open('lostcow.in') as f:
    lines = f.readlines()

file_input = list(map(int, lines[0].split()))

x, y = file_input
print(f'x = {x} y = {y}')

dirct = 1 if y >=x else -1
steps = [0, 1, -2, 4, -8, 16, -32, 64, -128, 256, -512, 1024, -2048]
distance = 0
prev_pos = x

for i in range(len(steps)):
    if (dirct == 1 and x + steps[i]>= y ) or (dirct == -1 and x+ steps[i]<= y):
        print(f'find Bessie!')
        distance += abs(y-next_pos) 
        break
    next_pos = x+steps[i]
    distance += abs(next_pos - prev_pos)
    prev_pos = next_pos
    print(f'loop i={i} pos = {prev_pos} distance={distance}')
    

print(f'distance = {distance}')
    
with open('lostcow.out','w') as f:
     f.write(str(distance))
    

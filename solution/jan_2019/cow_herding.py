from collections import defaultdict

with open('herding.in') as f:
    line = f.readlines()

location = [int(l) for l in line[0].split()]
location.sort()

a, b, c = location
print(f'{a} {b} {c}')

min_num = 0
max_num = 0

dist_1 = b-a
dist_2 = c-b

if dist_1 == 2 or dist_2 == 2: # only one empty location between a-b or b-c
    min_num = 1
else:
    min_num = 2

max_num = max(dist_1-1, dist_2-1)

if dist_1 == 1 and dist_2 == 1: # already together
    min_num = 0
    max_num = 0

print(f'{min_num} {max_num}')

with open('herding.out','w') as f:
     f.write(f'{min_num}\n')
     f.write(f'{max_num}\n')
     

with open('lifeguards.in') as f:
    lines = f.readlines()

N = int(lines[0])
guards_covered = []

for i in range(1, N+1):
   covered = [int(x) for x in lines[i].split()]
   guards_covered.append(covered)

print(guards_covered)

period_covered = [0] *1001
max_covered = 0

for covered  in guards_covered:
   print(f'{covered}')
   for i in range(covered[0], covered[1]):
      period_covered[i] += 1

total_covered = 0
# every lifeguards covered : no one is fired
for x in period_covered:
   if x > 0:
      total_covered += 1

print(f'{total_covered}')

# remove one lifeguard
for covered  in guards_covered:
   to_remove = 0
   for i in range(covered[0], covered[1]):
      if period_covered[i] == 1:
         to_remove += 1
   max_covered = max(max_covered, (total_covered-to_remove))
   
print(f'{max_covered}')
with open('lifeguards.out','w') as f:
    f.write(f'{max_covered}\n')
    
   

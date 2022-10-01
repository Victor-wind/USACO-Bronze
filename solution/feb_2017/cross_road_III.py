with open('cowqueue.in') as f:
    lines = f.readlines()

N = int(lines[0])
print(f'{N}')
last_time = 0

cows = [ [int(x) for x in lines[i].split()] for i in range(1, N+1)]
cows.sort()

print(f'{cows}')

for cow in cows:
   start, duration = cow[0], cow[1]
   if start < last_time:
      last_time += duration
   else:
      last_time = start + duration

print(f'{last_time}')

with open('cowqueue.out','w') as f:
    f.write(f'{last_time}\n')
    

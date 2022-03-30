with open('sleepy.in') as f:
    lines = f.readlines()

N = int(lines[0])
order = list(map(int, lines[1].split()))

i = N-1

while i > 0:
    if order[i] < order[i-1]:
        break
    else:
        i -= 1

with open('sleepy.out','w') as f:
     f.write(str(i))
    



with open('photo.in') as f:
    lines_N = f.readlines()
'''

lines_N = [1,1]
lines_N[0] = input()
lines_N[1] = input()
'''

N  = int(lines_N[0])
bn_str =  lines_N[1].split()

bn = [int(b) for b in bn_str]

an = [0]*1001

for i in range(1, N+1):
    an = [0]*1001
    an_set = set()
    an[0] = i
    k = 1
    for b in bn:
        an[k] = b - an[k-1]
        if an[k] in an_set or an[k] <= 0:
            break
        an_set.add(an[k])
        k += 1
    if k == N:
        break

res = str(an[0])
for i in range(1,N):
    res = res+" "+str(an[i])
    
res += '\n'
print(res)
        
with open('photo.out', 'w') as f:
    f.write(res)


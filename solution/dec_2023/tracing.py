N = int(input())
cows_str = input()

cows = [0] * (N+2)
for i in range(N):
    cows[i+1] =  int(cows_str[i])

#print(f"{N=} {cows=}")

# to solve it in O(N) times, introduce 2 lists to store the boundaries of infected cows

left_boundary = list()
right_boundary = list()

for i in range(1,N+1,1):
    if cows[i] == 1 and cows[i-1] == 0:
        left_boundary.append(i)
    if cows[i] == 1 and cows[i+1] == 0:
        right_boundary.append(i)
        
#print(f"{left_boundary=} {right_boundary=}")

condi = True
m, n = -1, -1
while condi:
    m, n = -1, -1
    # from boundaries move towards
    for i in range(len(left_boundary)):
        if cows[left_boundary[i]] == 1 and cows[left_boundary[i]+1] == 1:
            cows[left_boundary[i]] = 0
            left_boundary[i] +=1
        else:
            m = i; condi = False
            break

    if not condi: break
    m = len(left_boundary)

    for j in range(len(right_boundary)):
        if cows[right_boundary[j]] == 1 and cows[right_boundary[j]-1] == 1:
            cows[right_boundary[j]] = 0
            right_boundary[j] -= 1
        else:
            n = j; condi = False
            break

#print(f"{cows=}")
#print(f"{m=} {n=}")

# restore cows back
for i in range(m-1, -1, -1):
    boundary = left_boundary[i]-1
    cows[boundary] = 1

for i in range(n-1, -1, -1):
    boundary = right_boundary[i]+1
    cows[boundary] = 1

#print(f"{cows[1:-1:1]=}")
cnt = 0
for x in cows:
    if x == 1: cnt += 1

print(cnt)            

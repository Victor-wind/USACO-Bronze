# test cases 7-13 times out

N = int(input())
a = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]

checked_sum = [0] * N
numbers_by_op = [0] * (N+1)

total = 0
for i in range(N):
    if a[i] == b[i]: total += 1
    checked_sum[i] = total

def checks_by_index(checked_sum, i):
    if i < 0: return 0
    if i >= len(checked_sum): return checked_sum[-1]
    return checked_sum[i]

def expand(i, j):
    checks_middle = 0
    while i > -1  and j < N:
        if a[i] == b[j]: checks_middle += 1
        if a[j] == b[i]: checks_middle += 1
        if i==j and a[i] == b[j]: checks_middle -= 1
        checks_before_i = checks_by_index(checked_sum, i-1)
        checks_after_j = checks_by_index(checked_sum, N) - checks_by_index(checked_sum, j)
        total = checks_before_i + checks_middle + checks_after_j
        numbers_by_op[total]+= 1
        i -= 1
        j += 1
    
for i in range(N):
    expand(i,i)
    expand(i, i+1)  

for i in range(N+1):
    print(numbers_by_op[i])

# test cases 7-13 times out
N = int(input())
a = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]

checked_sum = [0] * N

total = 0
for i in range(N):
    if a[i] == b[i]:
        total += 1
    checked_sum[i] = total

def checks_by(checked_sum, i):
    if i < 0:
        return 0
    if i >= len(checked_sum):
        return checked_sum[-1]
    return checked_sum[i]

numbers_by_op = [0] * (N+1)
# checks result by the operation (l,r)
for l in range(N):
    for r in range(l,N):
        end = r
        checks_lr = 0
        for i in range(l, r+1):
            if a[i] == b[end]:
                checks_lr += 1
            end -= 1
        checks_before_l = checks_by(checked_sum, l-1)
        checks_after_r = checks_by(checked_sum, N) - checks_by(checked_sum, r) 
        checks = checks_before_l + checks_lr + checks_after_r
        numbers_by_op[checks]+= 1

for i in range(N+1):
    print(numbers_by_op[i])

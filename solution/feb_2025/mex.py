N = int(input())
a = [int(v) for v in input().split()]
#print(a)

# cnt[i]: the number of i appearing in list a
cnt = [0] * (N+1)
for i in a:
    cnt[i] += 1    

# missed[i]: how many integers missed in [0 : i-1] inclusive
missed = [0] * (N+1)
total_cnt = 0
for i in range(1,N+1):
    if cnt[i-1] == 0:
        total_cnt += 1
    missed[i] = total_cnt

for i in range(N+1):
    # in order to make the mex of a equal i, there are 2 conditions
    # a: zero i in list a
    # b: no missing integers [0, i-1] inclusive
    # so it needs missed[i] operations for condition b
    # and needs cnt[i] operations for condition a
    # if cnt[i] >= missed[i], only needs cnt[i] operations, as it converts missed[i] i integers into missed integers
    # if missed[i] > cnt[i], converts all cnt[i] i integers into missed integers,
    #    then do extra (missed[i] - cnt[i]) operation to satisfy remaining missed[i], so need missed[i] operations totally
    print(max(cnt[i], missed[i]))

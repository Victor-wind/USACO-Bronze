N, Q = [int(x) for x in input().split()]
close_time = [int(x) for x in input().split()]
arrive_time = [int(x) for x in input().split()]
diff = [close_time[i]-arrive_time[i] for i in range(N)]
#print(f'{N=} {Q=}')
diff.sort(reverse=True)
#print(f'{diff=}')
for _ in range(Q):
    V,S = [int(x) for x in input().split()]
    #print(f'{V=} {S=}')
    if diff[V-1] > S:
        print('YES')
    else:
        print('NO')

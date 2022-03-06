
N= int(input())

def check_merged_to(log,k,v):
    cnt = 0; res = 0
    merged_v = 0
    for l in log:
        if l > v: return -1
        if l == v:
            if merged_v != 0: return -1
        if l < v:
            merged_v +=l
            cnt += 1
            if merged_v == v:
                merged_v = 0; res += cnt-1; cnt = 0        

    if merged_v == 0: return res
    return -1
    

for j in range(N):
    k = int(input())
    log = input().split()
    for i in range(k):
        log[i] = int(log[i])

    sum_log = sum(log)
    max_log = max(log)

    #check whether it is possile to merge to a value in [max_log, sum_log]
    for v in range(max_log, sum_log+1):
        res = check_merged_to(log, k, v)
        if res >= 0:
            print(res)
            break
       


N= int(input())

def merge_check(log, val):
    cnt = 0
    sum_v = 0
    N = len(log)
    # print('merge_check  val=', val)
    for i in range(N):
        # print(' i ',i ,' cnt=', cnt)
        if log[i] == val and sum_v == 0: # No merge
            continue
        if log[i] == val and sum_v != 0: # could not merge to val
            return -1

        # merge val
        if sum_v != 0: cnt += 1 
        sum_v += log[i]        

        if sum_v == val: # good, merge to val
            sum_v = 0
        elif sum_v > val:# bad, could not merge to val
            return -1
        else:  # possile, continue to merge
            continue

    if sum_v != 0: # could not complete merge
        return -1    
    return cnt
   
for i in range(N):
    k = int(input())
    
    log = input().split()
    for j in range(k):
        log[j] = int(log[j])

    sum_log = sum(log)

    for merged_val in range(sum_log+1):
        # check whether merged_val could be the merged value
        cnt = merge_check(log, merged_val)
        if cnt >= 0:
            print("merged_val:", merged_val)
            break
        
    print(cnt)

'''
 
N= int(input())

def check_complete(log):
    N = len(log)
    if N < 2: return True
    for i in range(N):
        if not log[i] == log[0]: return False
    return True
   
def merge_cnt(k,log, cnt):
    if len(log) < 2: return cnt
    if len(log) == 2:
        if log[0] == log[1]: return cnt
        if log[0] != log[1]: return cnt+1

    # add some optimization: if head or tail is not max_value, must merge head/tail
    max_v = max(log)
    while log[0]!=max_v or log[-1]!=max_v:
        if log[0]!=max_v:
            log = [log[0]+log[1]]+log[2:]
            cnt +=1
        elif log[-1]!=max_v:
            log = log[:-2]+[log[-1]+log[-2]]
            cnt +=1
        max_v = max(max_v, log[0], log[-1])
        if len(log) < 2: return cnt
        if len(log) == 2:
            if log[0] == log[1]: return cnt
            if log[0] != log[1]: return cnt+1

    if check_complete(log): return cnt

    N = len(log)
    if len(log) < 2: return cnt
    if len(log) == 2:
        if log[0] == log[1]: return cnt
        if log[0] != log[1]: return cnt+1
    
    index = 1
    for i in range(1, N-1):
        if log[i] != log[0]:
            index = i
            break

    log_1 = log[:i]+[log[i]+log[i+1]]+log[i+2:]
    log_2 = log[:i-1]+[log[i-1]+log[i]]+log[i+1:]

    x1 = merge_cnt(len(log_1),log_1, cnt+1)
    x2 = merge_cnt(len(log_2),log_2, cnt+1)
     
    return min(x1, x2)

for j in range(N):
    k = int(input())
    log = input().split()
    for i in range(k):
        log[i] = int(log[i])
    x = merge_cnt(k, log, 0)
    print(x)

 '''

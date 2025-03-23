# the official solution is clear.
# Observation: given a lsit and a number cnt, if len(lst) % cnt == 0 and lst[:-cnt] == lst[cnt:]
# lst has repeated pattern of lst[0:cnt].  <- (lst[0], lst[1], lst[2], ... lst[cnt-1] ) == (lst[cnt], lst[cnt+1], ... lst[cnt+cnt-1])
# (lst[cnt], lst[cnt+1], ... lst[cnt+cnt-1] ) == (lst[2*cnt], lst[2*cnt+1], ... lst[2*cnt+cnt-1])
# (lst[2*cnt], lst[2*cnt+1], ... lst[2*cnt+cnt-1] ) == (lst[3*cnt], lst[3*cnt+1], ... lst[3*cnt+cnt-1])
# ...

T = int(input())

def solution_K1(seq, N):
    if N == 0: return True
    # check all elements of seq equal
    return seq[1:] == seq[:-1]

def solution_K2(seq, N):
    # complexity O(N)
    if solution_K1(seq, N):
        return True
    left = 0
    right = 0
    while right < N and seq[right] == seq[left]:
        right += 1
    cnt1 = right - left
    left = right
    while right < N and seq[right] == seq[left]:
        right += 1
    cnt2 = right - left
    cnt = cnt1 + cnt2
    if N % cnt == 0 and seq[cnt:]==seq[:-cnt]:
        return True
    return False

def solution_K3(seq, N):
    if solution_K2(seq, N): return True
    # divide list seq in multiple sub_list with len i=[2:N//2+1].
    # If seq[0:i] is a repeated pattern, furthur divide seq[0:i] and verify its sub_list is K1 or K2
    sub_lst_size = list(range(2, N//2+1)) + [N]
    for i in sub_lst_size:
        if N % i != 0 or seq[i:] != seq[:-i]: continue
        sub_seq = seq[0:i]
        for j in range(1,i): # divide furthur
            str_1 = sub_seq[:j]
            str_2 = sub_seq[j:]
            n1 = j
            n2 = i-j
            if solution_K1(str_1, n1) and solution_K2(str_2, n2):
                return True
            if solution_K2(str_1, n1) and solution_K1(str_2, n2):
                return True
    return False
    

for _ in range(T):
    N, K = [int(x) for x in input().split()]
    #print(f'{N=} {K=}')
    seq = [int(x) for x in input().split()]
    #print(seq)
    res = False
    if K == 1:
        res = solution_K1(seq,N)
    elif K == 2:
        res = solution_K2(seq,N)
    else:
        res = solution_K3(seq,N)
    if res:
        print('YES')
    else:
        print('NO')
  

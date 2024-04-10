def construct_permutation(N, h):
    seq = [0]*(N+1)
    # find the 2 numbers at the end of seq from h[:-1]
    # the 2 numbers missing from h[:-1] are the end numbers of seq
    for i in range(N-2):
        seq[h[i]] = 1
    end_lst = [i for i in range(1,N+1) if seq[i]!=1]
    #print(f'{end_lst=}') 
    if len(end_lst) != 2 or (N == 2 and h[0] != 1): 
        print(-1)
        return
    
    used_num = set(end_lst)
    # if swapping seq[1]/seq[N], we can build another seq_2 (seq_2 is reversed seq)
    # the question asks for lexicographically small solution, so let seq[1] < seq[N] 
    seq[1] = min(end_lst); seq[N] = max(end_lst);
    left = 1; right = N
    total_num = 2
    for k in range(N-2):
        x = h[k]
        if x in used_num: break
        used_num.add(x)
        if seq[left] < seq[right]:
            right -= 1 
            seq[right] = x
        elif seq[left] > seq[right]:
            left += 1
            seq[left] = x
        else:
            break
        total_num += 1 
    # check the last item in h
    if h[-1] != min(seq[left],seq[right]):
        print(-1)        
    elif total_num == N:
        print(*seq[1::])
    else:
        print(-1)

T = int(input())
for _ in range(T):
    N = int(input())
    h = [ int(x) for x in input().split()] 
    # print(f'{N=} {h=}')
    construct_permutation(N, h)

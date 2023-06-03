N, K, T = [int(x) for x in input().rstrip().split()]
A = [int(x) for x in input().rstrip().split()]

#print(f'{N=} {K=} {T=}')
#print(f'{A=}')

output = [i for i in range(N)]

def update_pos(output: list, A: list, N: int, K: int) -> list:
    temp = output[A[K-1]]
    for i in range(K-2,-1,-1):
        src = A[i]
        dst = A[i+1]
        output[dst] = output[src]
    output[A[0]] = temp
    A = [(i+1)%N for i in A]
    print(f'in update_pos {A=} {output=}')
    return A

for _ in range(T):
    A = update_pos(output, A, N, K)

output = [str(x) for x in output]
print(' '.join(output))
    

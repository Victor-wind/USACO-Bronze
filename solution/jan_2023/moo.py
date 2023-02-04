import sys

def cnt_moo(s: str):
    n = len(s)
    if n < 3: return -1
    
    # n >= 3: at least needs n-3 operations to reduce the size to 3
    # since the deletion can only happen at both ends.
    # only need to check 'MOO', 'MOM', 'OOO', 'OOM'
    if 'MOO' in s:
        return n-3
    if 'MOM' in s or 'OOO' in s:
        return n-3+1
    if 'OOM' in s:
        return n-3+2
    # could not do it
    return -1


N = int(input())

for i in range(N):
    s = input()
    cnt = cnt_moo(s)
    print(cnt)

# Binary search time out, have to use hash table. The binary search is commented out at the end for reference.
# My solution has better execution time than the official solution, as pre-processing is simpler 

import string

N, Q = [int(i) for i in input().split()]
#print(N, Q)

description = input()

# left[i]['c'-'a'] stores the largest index k of char 'c' for description[0, i] inclusive; it is the index of 'c' closest to index i from left side   
left = [[-1]*26 for _ in range(N)]
# right[i]['c'-'a'] stores the smallest index k of char 'c' for description[i, N-1] inclusive; it is the index of 'c' closest to index i from right side 
right = [[N]*26 for _ in range(N)]
# right_exclude[i]['c'-'a'] stores the smallest index k of a (any) char (not 'c') for description[i, N] inclusive; it is the index of non-'c' char closest to index i from right side 
right_exclude = [[N]*26 for _ in range(N)]

for index, c in enumerate(description):
    k = ord(c) - ord('a')
    left[index] = left[index-1][:] if index else [-1]*26
    left[index][k] = index

for i in range(N-1,-1, -1):
    k = ord(description[i]) - ord('a')
    right[i] = right[i+1][:] if i != N-1 else [N]*26
    right[i][k] = i
    
    right_exclude[i] = right_exclude[i+1][:] if i != N-1 else [N]*26
    for j in range(26):
        if j != k:
            right_exclude[i][j] = i

def solution(l, r):
    # i, j , k
    # for the optimal (i,j,k) k should be last char 'x' closest to r from left. If there is another 'x' with index z closer to r, then (z-j)*(j-i) > (k-j)*(j-i), which is not possible.
    # so iterate 26 chars of k closest to r, then find the leftest non-k char to build (i,.,k), then choose the best of these 27 values.
    # left[m][t] is the index closest to mid (i+k)//2 from left side,  right[m][t] is the index closest to mid (i+k)//2 from right side. j must be one of it. 
    max_v = -1
    for t in range(26):
        k = left[r][t]
        i = right_exclude[l][t]
        if i >= k-1: continue
        # find the middle index
        m = (i+k)//2
        for u in (left[m][t], right[m][t], left[m+1][t], right[m+1][t]):
            max_v = max(max_v, (k-u)*(u-i))
    return -1 if max_v<=0 else max_v
        
        
for _ in range(Q):
    l, r = [int(i) for i in input().split()]
    l -= 1
    r -= 1
    print(solution(l, r))    
    


'''
# build a dic to store index of each char
pos_dict = {c: [] for c in string.ascii_lowercase}
for i in range(N):
    pos_dict[description[i]].append(i)
#print(pos_dict)


# find the largest index in lst, lst[index] <= target
# if all > target, return -1; if all < target, return len(lst)-1
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right


def max_value(index, lst, l, r):
    if (r - l) < 1:
        return -1
    if l < 0 or r >= len(lst):
        #print(f'should not happen! {l=} {r=} {lst=}')
        return -1
    value = 0
    for m in range(l, r):
        p = lst[m]
        if p <= index: print('should not happen 2!')
        t = (p - index) * (lst[r] - p)
        if t > value: value = t
    return value

def max_value_bsearch(index, lst, l, r):
    if (r - l) < 1:
        return -1
    if l < 0 or r >= len(lst):
        #print(f'should not happen! {l=} {r=} {lst=}')
        return -1
    pos_1 = index
    pos_3 = lst[r]
    target = (pos_1+pos_3)//2
    # middle 'o' should be (pos_1+pos_3)//2 or (pos_1+pos_3)//2+1
    # binary search for the index whose value is <= (pos_1+pos_3)//2
    index_m = binary_search(lst, target)
    value_1 = (lst[index_m] - index) * (lst[r] - lst[index_m])
    index_m += 1
    value_2 = (lst[index_m] - index) * (lst[r] - lst[index_m])
    if value_1 > value_2:
        return value_1
    return value_2

    
def solution(l, r):
    max_v = -1
    visited = set()
    for index in range(l, r):
        c = description[index]
        if c in visited:
            continue

        visited.add(c)

        # check whether c could make moo with a char in string.ascii_lowercase
        for o in string.ascii_lowercase:
            lst = pos_dict[o]

            # print(f'Debug1 {l=} {r=} {c=} {o=} {lst=} {index=}')

            if o == c or len(lst) == 0: continue

            lst_right = binary_search(lst, r)

            # print(f'Debug1 {l=} {r=} {c=} {o=} {lst=} {lst_right=} {index=}')
            if lst[lst_right] <= index + 1:  # not enough o to make 'moo'
                continue

            lst_left = binary_search(lst, index + 1)
            if lst_left == -1 or lst[lst_left] != (index + 1):
                lst_left = lst_left + 1
            # index within [lst_left, lst_right] can make 'moo'
            # print(f'Debug2 {l=} {r=} {c=} {o=} {lst=} {lst_left=}')
            # value = max_value(index, lst, lst_left, lst_right)
            value = max_value_bsearch(index, lst, lst_left, lst_right)
            if value > max_v:
                max_v = value
                
            if len(lst) == 26: # don't need to continue
                break

    return max_v


for _ in range(Q):
    l, r = [int(i) for i in input().split()]
    l -= 1
    r -= 1
    print(solution(l, r))

'''

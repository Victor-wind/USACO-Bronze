'''
Divide the statement into groups of 'or' (groups_or). Within a group, its elements are 'and'.
groups_or is a list of list. each sub-list includes the index of a group elements.
val_before and val_after are lists including True/False eval before the groups.
val_before[100] = True means there is a True group before pos 100.
val_after[200] = True means there is a True group after pos 200.
func find_index is to find the group index for element idx.
For query (l,r,res), we can find the associated group_left_idx in which l resides;
and group_right_idx in which r resides.
From val_before[l] we know whether there is a True group before l;
From val_after[r] we know whether there is a True group after r;
We also can merge the groups between [group_left_idx, group_right_idx].
To get constant time complex, we need to know whether the first False in groups_false_pos[group_left_idx] is before l;
and whether the last False in groups_false_pos[group_right_idx] is after r.
In either case, the merged group must be evalued to False;
otherwise, the merged group could be evalued to the desired boolean value res
'''
def eval_group(lst):
    bool_lst = [ True if statement[idx] == 'true' else False for idx in lst]
    return all(bool_lst)

def find_index(idx):
    left = 0; right = len(groups_or)
    while left <= right:
        middle = (left+right)//2
        if groups_or[middle][0]<= idx <= groups_or[middle][-1]:
            return middle
        elif idx > groups_or[middle][-1]:
            left = middle+1
        else:
            right = middle-1
    return None

N,Q = [int(x) for x in input().split()]
statement = input().split()
#print(f'{statement=}')
# split statement into groups of 'or'
groups_or = list()
and_lst = list()
for i in range(N):
    if statement[i] == "and":
        pass
    elif statement[i] == "or":
        groups_or.append(and_lst)
        and_lst = list()
    else: # put index for func find_index
        and_lst.append(i)
groups_or.append(and_lst)

val_res = False
val_before = [False]*N; val_after = [False]*N
for lst in groups_or:
    first_idx = lst[0]
    val_before[first_idx] = val_res
    val_res = val_res or eval_group(lst)    
val_res = False
for lst in groups_or[::-1]:
    idx = lst[-1]
    val_after[idx] = val_res
    val_res = val_res or eval_group(lst)
#print(f'{val_before=}')
#print(f'{val_after=}')

# groups_false_pos stores the first and last False pos for each group
groups_false_pos = list()
for lst in groups_or:
    first_pos=None;last_pos=None
    for idx in lst:
        if statement[idx] == 'false' and first_pos is None:
            first_pos = idx
        if statement[idx] == 'false':
            last_pos = idx
    groups_false_pos.append([first_pos,last_pos])  
#print(f'{groups_false_pos=}')         

solution = list()
for _ in range(Q):
    l, r, res = input().split()
    l = int(l)-1; r = int(r)-1;
    res = True if res=='true' else False
    group_left_idx = find_index(l)
    group_right_idx = find_index(r)
    eval_before = val_before[groups_or[group_left_idx][0]]
    eval_after = val_after[groups_or[group_right_idx][-1]]
    eval_merged = res
    if groups_false_pos[group_left_idx][0] is not None and groups_false_pos[group_left_idx][0] < l:
        eval_merged = False
    if groups_false_pos[group_right_idx][1] is not None and groups_false_pos[group_right_idx][1] > r:
        eval_merged = False        
    #print(f"   {eval_before=} {eval_after=} {eval_merged=}")
    if (eval_before or eval_after or eval_merged) == res:
        solution.append('Y')
    else:
        solution.append('N')

print(''.join(solution))

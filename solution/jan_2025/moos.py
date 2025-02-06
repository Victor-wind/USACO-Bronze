N = int(input())
a = [int(v) for v in input().split()]
#print(a)
#print(N)

cnt_right = [0] * (N-1)

for v in a:
    cnt_right[v] += 1   

total = 0
dist_left = set() # it can use a list as set to count the distinct numbers as well
for i, v in enumerate(a):
    # when cnt_right[v] == 2, there are only one num v after index i, 
    # so combine disct numbers before index i with 2 v to get moo (x, v, v)
    # there is only one index i: cnt_right[a[i]] == 2 -> No i2: a[i] = a[i2] && cnt_right[a[i2]] == 2
    if cnt_right[v] == 2:
        # if v is already in dist_left, reduce the cnt by 1
        total += len(dist_left) - int(v in dist_left)
    cnt_right[v] -= 1
    dist_left.add(v)

print(total)

# The above solution combines all disct numbers (x) BEFORE index i (v) to get moo (x, v, v);
# The complementary search also works: enumerate array, for each unique x, combines all disct number pairs (v, v) AFTER it.

N = int(input())
patches = [int(x) for x in input().split()]
#print(f"{N=} {patches=}")
applications = 0

def cal_applications(times, patches, i):
    to_add = -times
    acc_add = to_add
    N = len(patches)
    for j in range(i, N, 1):        
        patches[j] += acc_add
        acc_add += to_add
        
'''
For minimum number of applications, the order applied does not matter.
We can make patches[0] to 0, then patches[1], patches[2], ... patches[N]
test cases 11 - 15 time out
# O(N^2) time complexity
for i in range(N):
    v = patches[i]    
    if v == 0:
        continue    
    applications += abs(v)    
    cal_applications(v, patches, i)    
    #print(f"{i=} {patches=} {applications=}")
'''

'''
Optimized solution, O(N) time complexity
if add L bacteria at patch[i], then a(i) -> L(i), 2L(i+1), 3L(i+2), 4L(i+3), 5L(i+4), ... ?(N-1)
if add M bacteria at patch[i+2], then b(i) ->               M(i+2), 2M(i+3), 3M(i+4), ... ?(N-1)
at patch i+k (k>2), sum a(i)+b(i),     c(i+1) = c(i) + L+M
'''
acculated_applies = 0
to_apply = 0
for i in range(N):
    # print(f"{patches[i]=} {acculated_applies=} {to_apply=}")
    patches[i] += acculated_applies
    applications += abs(patches[i])
    to_apply += -patches[i]
    acculated_applies += to_apply
    acculated_applies += -patches[i]
    
print(applications)


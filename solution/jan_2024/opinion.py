'''
for 3 contiguous cows [i,i+1,i+2], if there is a majority opinion hay type X,
all N cows could agree on type X by extending the range to left or right : [i,i+2] -> [i,i+3] -> [i,i+4] ... [i,N]

for any focus groups [i, i+2K+1] with majority opinion hay type X,
cows group [i, i+K+1], or [i+K+1, i+2K+1] must have majority opinion hay type X: 
if they don't, [i, i+K+1] have at most K/2 cows with opinion type X, [i+K+1, i+2K+1] have at most K/2.
[i, i+2K+1] have at most K, which is not possible.
Follow this process we can reach 3 contiguous cows case.
So we conclude for any focus groups, only need to check 3 contiguous cows case.
'''

def find_hays(n, cows):
    hays = set()
    for i in range(N-2):
        compare = [cows[i],cows[i+1],cows[i+2]]
        compare.sort()
        if compare[0] == compare[1] or compare[2] == compare[1]:
            hays.add(compare[1])
    # corner case: only 2 cows
    if len(cows) == 2 and cows[0] == cows[1]:
        hays.add(cows[0])
      
    hays = list(hays)
    if not hays:
        hays.append(-1)
    hays.sort()

    print(*hays)

T = int(input())
for _ in range(T):
    N = int(input())
    cows = [ int(x) for x in input().split()]
    # print(f" {N=} {cows=}")
    find_hays(N, cows)

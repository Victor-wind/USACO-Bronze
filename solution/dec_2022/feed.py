import sys

#f = open("test.txt", "r")
f = sys.stdin

T = int(f.readline())

def getpatch_from_end(N:int, patch: list):
   i = N-1
   while i >=0:
      if patch[i] == '.':
         break
      i -= 1
   return i

# if the cows move to the full distance i+K, there is no conflict: H and G will not move to the same position as they start from different position. 
# when reaching the end, H / G may not move to full distance because of boundary limit i+K >= N. So conflict is possible. 
# in this case, the cows need to use the empty slots from the end. 
# the conflict may happen in 2 cases: 1. a cow moves to i+K from i, but [i+K] is occupied by another cow, who could not move to full distance. 
# 2. a cow could not move to full distance, so it searches backward from the end till finding an empty patch. 
# in both cases, the greedy algorithm still works, as explained below. 

# Case 1: H wants to move from [i] to [i+K], but [i+K] is occupied by G, as G did not move to  full distance. 
#         we should know that [i+K] should be the last slot [N-1], since short moves only happens at most once for H and G. 
#         H searches backward from [N-1], and [N-1] is occupied by G. it should use [N-2], which should be empty. 
# Case 2: H wants to move from [i] to [i+K], but [i+K] is beyound boundary: i+K >= N. So it needs search back from the end. 
#         Any slot from [i] to [N-1] should be good for H. 
#         patch [i] is good enough for H (i+K>N), if patch [i] is occupied by G, then patch [i+1] (i+1 is not the last one) is empty.
#         if i is the last one and occupied by G, then patch [i-1] (N-2) is empty and good for H.   

def allocate_patch_cow(cows: str, N: int, K: int, patch: list, H_G: str):
   cnt = 0
   i = 0
   while i < N:
      if cows[i] == H_G:
         cnt += 1
         if i+K < N:
            if patch[i+K] == '.':
               patch[i+K] = H_G
               i += (K+K)
            else:
               x = getpatch_from_end(N, patch)
               patch[x] = H_G
               break
         else: # put it at the end
            x = getpatch_from_end(N, patch)
            patch[x] = H_G
            break            
      i += 1
   return cnt
               

for _ in range(T):
   N, K = [ int(x) for x in f.readline().split()]
   cows = f.readline()
   patch = ['.'] * N
   n1 = allocate_patch_cow(cows, N, K, patch, 'H')
   n2 = allocate_patch_cow(cows, N, K, patch, 'G')
   print(n1+n2)
   print(''.join(patch))
  

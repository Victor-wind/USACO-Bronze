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
  

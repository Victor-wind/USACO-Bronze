with open('cownomics.in') as f:
    lines = f.readlines()

N, M = (int(x) for x in lines[0].split())

print(f'{N} {M}')

spotty_cows = lines[1: 1+N]
plain_cows = lines[1+N::]
pos_cnt = 0

# print(f'{spotty_cows=} \n\n{plain_cows=}')
   
def CountPos(spotty: list, plain: list, k: int, n: int ) -> bool:
   spotty_set = set()
   plain_set = set()

   for i in range(n):
      spotty_set.add(spotty[i][k])
      plain_set.add(plain[i][k])

   if len(spotty_set & plain_set) > 0 :
      return False
   
   return True

for i in range(M):
   if CountPos(spotty_cows, plain_cows, i, N):
      pos_cnt += 1

   
print(f'{pos_cnt}')
with open('cownomics.out','w') as f:
    f.write(f'{pos_cnt}\n')

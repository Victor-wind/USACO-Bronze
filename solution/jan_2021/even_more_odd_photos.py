import sys
import time

N = input()
ids = input()

id_list = ids.split()

odd = 0
even = 0

for id in id_list:
    if int(id) % 2 == 0:
        even += 1
    else:
        odd += 1

groups = 0

even_t = even
odd_t  = odd

while odd_t > even_t:
    odd_t -= 2
    even_t += 1

if even_t >= odd_t+1:
    groups = 2*odd_t+1
elif even_t == odd_t:
    groups = 2*odd_t

print(groups)





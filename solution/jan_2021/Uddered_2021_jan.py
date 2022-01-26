import sys
import time

cowphabet = input()
song = input()

cow_map = {}

for i in range(len(cowphabet)):
    cow_map[cowphabet[i]] = i

cnt = 1
prev_index = -1
for c in song:
   if cow_map[c] > prev_index:
       prev_index = cow_map[c]
   else:
       prev_index = cow_map[c]
       cnt += 1

print(cnt)

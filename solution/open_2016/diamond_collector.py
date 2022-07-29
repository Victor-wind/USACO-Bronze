diamonds.sort()

print(diamonds)

max_cnt = 1

'''
# two loops
for i in range(N):
   cnt = 1
   for j in range(i+1, N):
      if diamonds[j] > diamonds[i] + K:
         break
      cnt += 1
   max_cnt = max(max_cnt, cnt)
'''

# sliding window
max_cnt = 1
left = 0
for right in range(N):
   if diamonds[right] <= diamonds[left] + K :
      max_cnt = max(max_cnt, right-left+1)
   else:
      while diamonds[right] > diamonds[left] + K:
         left += 1    

print(max_cnt)
with open('diamond.out','w') as f:
    f.write(f'{max_cnt}\n')

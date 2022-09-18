with open('circlecross.in') as f:
    lines = f.readlines()

cross_pairs = 0

#print(f'{lines[0]}')

points = dict()

for i in range(26):
   key = chr(ord('A')+i)
   points.update( {key: []})

for i in range(52):
   key = lines[0][i]
   points[key].append(i)
   
#print(f'{points}')

for i in range(26):
   key = chr(ord('A')+i)
   s, e = points[key]
   #print(f'{lines[0][s:e+1]}')
   for c in lines[0][s:e+1]:
      s1, e1 = points[c]
      if s1 < s or e1 > e:
         cross_pairs += 1
   
#print(f'{cross_pairs}')

with open('circlecross.out','w') as f:
    f.write(f'{cross_pairs//2}\n')

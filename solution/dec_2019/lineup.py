
with open('lineup.in') as f:
    lines_N = f.readlines()

cows = ['Sue', 'Bessie', 'Buttercup', 'Belinda', 'Beatrice',
        'Bella', 'Blue', 'Betsy']

cows.sort()
cow_nums = ['1','2','3','4','5','6','7','8']

cows_to_num = dict(zip(cows,cow_nums))

#print(cows_to_num)

'''
lines = ['Betsy must be milked beside Belinda',
         'Buttercup must be milked beside Sue',
         'Beatrice must be milked beside Bessie',
         'Betsy must be milked beside Sue'
         ]


lines = ['Sue must be milked beside Bessie',
         'Sue must be milked beside Beatrice',
         'Beatrice must be milked beside Betsy',
         'Bella must be milked beside Bessie'
         ]
'''

lines = lines_N[1::]

relations = []

for line in lines:
    line_list = line.split()
    nums = [ cows_to_num[line_list[0]]+cows_to_num[line_list[-1]], cows_to_num[line_list[-1]]+cows_to_num[line_list[0]]]
    relations.append(nums)
    
print(relations)

N = len(relations)

for i in range(N):
    for j in range(N):
        if i == j or relations[i] == None or relations[j] == None:
            continue        
       
        # there are 8 combinations, but only 2 are possile.
        new_combine = []
        for r1 in relations[i]:
            for r2 in relations[j]:
                if r1[-1] == r2[0]:
                    x = r1+r2[1:]
                    new_combine.append(x)
                if r2[-1] == r1[0]:
                    x = r2+r1[1:]
                    new_combine.append(x)
        if len(new_combine) > 0:
            relations[i] = new_combine
            relations[j] = None
        
        #print("in loop: ", relations)

print("after merge:", relations)

sorted_relation = []
for r in relations:
    if r is not None:
        r.sort()
        sorted_relation.append(r[0])
        
#print(sorted_relation)

for r in sorted_relation:
    #print(r)   
    for c in r:
        index = ord(c)- ord('1')
        cow_nums[index] = None
        
print(cow_nums)

for cow in cow_nums:
    if cow is not None:
        sorted_relation.append(cow)

sorted_relation.sort()
print(sorted_relation)

with open('lineup.out', 'w') as f:
    for r in sorted_relation:
        for c in r:
            k = ord(c)-ord('1')
            print(cows[k])
            f.write(cows[k]+'\n')

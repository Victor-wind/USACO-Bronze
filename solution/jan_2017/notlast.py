from collections import defaultdict

cows = defaultdict(int)

names = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle',
         'Maggie',  'Henrietta']

for n in names:
    cows[n] = 0

with open('notlast.in') as f:
    lines = f.readlines()

N = int(lines[0])

for l in lines[1:]:
    name, milk = l.split()
    cows[name] += int(milk)

print(cows)
# convert cows dict to list in order to sort
cows_list = [ [milk, cow] for cow, milk in cows.items() ]

cows_list.sort()

result = 'Tie'
milk = cows_list[0][0]

i = 1
for i in range(1, 7):
    if cows_list[i][0] != cows_list[0][0]:
        break

if i == 6 and cows_list[6][0] != cows_list[0][0]:
    result = cows_list[6][1]

if i != 6 and cows_list[i][0] != cows_list[i+1][0]:
    result = cows_list[i][1]
    

print(f'{cows_list}')

print(f'{result}')

with open('notlast.out','w') as f:
     f.write(f'{result}\n')
     

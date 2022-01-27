N = int(input())

cows = {}
years_animal= { 'Ox' : 0, 'Tiger': 1, 'Rabbit':2, 'Dragon':3,
                'Snake':4, 'Horse':5, 'Goat':6, 'Monkey':7,
                'Rooster':8, 'Dog':9, 'Pig':10, 'Rat':11}

for i in range(N):
    s = input()
    info = s.split()
    # print(info)
    cow = {'born': info[4], 'comparedTo': info[7], 'relative':info[3], 'to_year': None, 'to_Bessie_age': None}
    cows[info[0]] = cow

cows['Bessie'] = {'born': 'Ox', 'comparedTo': 'Bessie', 'relative':None, 'to_year': 0, 'to_Bessie_age': 0}

#print(cows)

#get relative years
for cow, info in cows.items():
    cow_born = years_animal[(info['born'])]
    another_cow  = info['comparedTo']
    another_born = years_animal[cows[another_cow]['born']]
    
    relative_year = (cow_born) - another_born
    if relative_year <= 0:
        relative_year += 12

    if info['relative'] == 'previous':
        relative_year = cow_born - (another_born)
        if relative_year>=0:
            relative_year -= 12
        
    info['to_year'] = relative_year


while N > 0:
    for cow, info in cows.items():
        if cow == 'Bessie' or info['to_Bessie_age'] is not None:
            continue
        another_cow  = info['comparedTo']
        to_Bessie_age = cows[another_cow]['to_Bessie_age']
        if to_Bessie_age is not None:
            info['to_Bessie_age'] = to_Bessie_age + info['to_year']
            N -=1
'''
for cow, info in cows.items():
    print(cow)
    print(info)
    print('\n')
'''

print(abs(cows['Elsie']['to_Bessie_age']))

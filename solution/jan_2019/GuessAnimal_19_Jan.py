with open('guess.in') as f:
    lines = f.readlines()

N = int(lines[0])

animals = {}
# process input data
for i in range(N):
    t = lines[i+1].split()
    animals[t[0]] = set(t[2::])

print(animals)

# for each animal, find the most 'yes' it could get
# then select the animal with the most 'yes'
most_yes_by_animal = list()
for x in animals:
    cnt_x = 0
    # for given animal x, it could have at most len(animals[x]) 'Yes'
    # for its best solution, the feasible set contains all animals at beginning.
    # with questions ongoing, the animals are removed from the feasible set gradually
    # till only animal x and y are in the set
    # the max 'Yes' is animals[x] & animals[y]
    # for all possible animal y, find the best one together with the given animal x   
    for y in animals:        
        if x == y: continue
        z = animals[x] & animals[y]
        cnt_x = max(cnt_x, len(z))
    most_yes_by_animal.append(cnt_x) 
        
result = (max(most_yes_by_animal)+1)
print(result)
with open('guess.out','w') as f:
     f.write(f'{result}')

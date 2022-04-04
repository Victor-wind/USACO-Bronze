with open('guess.in') as f:
    lines = f.readlines()

N = int(lines[0])

animals = {}
# process input data
for i in range(N):
    t = lines[i+1].split()
    animals[t[0]] = t[2::]

#print(animals)

max_yes = 1

for x in animals:
    for y in animals:
        if x == y: continue
        z = set(animals[x]) & set(animals[y])
        max_yes = max(max_yes, len(z)) 
        
#print(max_yes+1)
with open('guess.out','w') as f:
     f.write(str(max_yes+1))
    



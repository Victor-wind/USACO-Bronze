
with open('shell.in') as f:
    lines = f.readlines()

N = int(lines[0])
guess = []

for i in range(N):
    a, b, c = map(int, lines[i+1].split())
    guess.append([a,b,c])
    
max_score = 0
pebbles   = [0, 1, 2]
guess_cnt = [0] *3


for i in range(N):
    a, b, c = guess[i]
    pebbles[a-1], pebbles[b-1] = pebbles[b-1], pebbles[a-1]
    pebble = pebbles[c-1]
    guess_cnt[pebble] += 1

max_score = max(guess_cnt)

#print(max_score)

with open('shell.out','w') as f:
     f.write(str(max_score))

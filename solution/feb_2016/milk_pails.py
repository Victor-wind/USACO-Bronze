f = open('pails.in')
lines = f.readlines()
lines = lines[0].split()
print(lines)
x = int(lines[0])
y = int(lines[1])
M = int(lines[2])
#print(f'{x=} {y=} {M=}')
max_milk = 0

for i in range(M//x+1):
    for j in range(M//y+1):
        n = x*i + y*j
        if n<=M:
            if n>=max_milk:
                max_milk = n

print(max_milk)

f = open('pails.out','w')
f.write(str(max_milk))

# contributed by lazy panda

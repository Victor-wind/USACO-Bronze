f = open('blocks.in')
lines = f.readlines()
f.close()
N = int(lines[0])
blocks = []
for i in range(1,N+1):
    x = lines[i].split()
    blocks.append(x)

#print(blocks)

result = [0]*26

def calculate(str1,str2,result):
    list1,list2 = [0]*26, [0]*26
    for x in str1:
        index = ord(x)-ord('a')
        list1[index]+=1
    for y in str2:
        index = ord(y)-ord('a')
        list2[index]+=1
    for i in range(26):
        result[i]+=max(list1[i], list2[i])

f = open('blocks.out','w')

for block in blocks:
    calculate(block[0],block[1],result)

for x in result:
    f.write(f'{x}\n')

f.close()
    
# contributed by Ves Panda
    



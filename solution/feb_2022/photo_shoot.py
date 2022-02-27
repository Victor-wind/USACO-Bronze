from collections import Counter

N= int(input())
an = input().split()
bn = input().split()

an_p = 0
bn_p = 0

an_counter = Counter(an)

# print(an_counter)

def search_replace(x):
    global an_counter
    if x in an_counter:
       an_counter[x] = None 
       return

cnt = 0

for i in range(N):    
    while an_counter[an[an_p]] is None:
        an_p += 1        
    if bn[bn_p] != an[an_p]:
        #print("bn_p =", bn_p, " bn[bn_p]=",bn[bn_p])
        #print("an_p =", an_p, " an[an_p]=",an[an_p])
        #print(an)
        cnt += 1
        search_replace(bn[bn_p])
        bn_p += 1
    else:
        an_p +=1
        bn_p +=1
    
print(cnt)
    

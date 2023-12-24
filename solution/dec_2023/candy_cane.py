N, M = [ int(x) for x in input().split()]
heights_cow = [ int(x) for x in input().split()]
heights_cane = [ int(x) for x in input().split()]

#print(f' {heights_cow=} {heights_cane=}')
for i in range(M):
    cane_h, cane_l = heights_cane[i], 0    
    for j in range(N):
        if heights_cow[j] > cane_l:
            eat = min(cane_h,heights_cow[j]) - cane_l
            heights_cow[j] += eat
            cane_l += eat
        # if the whole candy is eaten, break the loop
        if cane_h == cane_l:
            break        

for h in heights_cow:
    print(h)

N = input()
heights_str = input()
stalls_str= input()

N = int(N)

heights = heights_str.split()
heights = [int(h) for h in heights]
heights.sort(reverse=True)

stalls = stalls_str.split()
stalls = [int(s) for s in stalls]
stalls.sort(reverse=True)

#print(N)
#print(heights)
#print(stalls)

cnt = 0

def cal_cnts(heights, stalls):
    K = len(stalls)
    if len(heights) != len(stalls):
        return -1
    
    cnt = 1
    reduce = 0

    for h in heights:
        x = K
        for i, value in enumerate(stalls):
            if value < h:
                x = i
                break
        cnt *= (x-reduce)
        #print("h = {} x {}".format(h, (x-reduce)))
        reduce +=1
        
    return cnt

cnt = cal_cnts(heights, stalls)
if cnt <= 0:
    cnt = 0
    
print(cnt)

        



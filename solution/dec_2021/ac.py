
N= int(input())

cur_temp = input().split()
target_temp = input().split()

adjust = [ int(cur_temp[i])-int(target_temp[i]) for i in range(N)]

cnt = 0

def sig_v(v):
    if v > 0: return 1
    if v < 0: return -1
    return 0

def adjust_temp(temperature, i, N):
    cnt = abs(temperature[i])
    while temperature[i] != 0:
        inc = sig_v(temperature[i])
        times = 1000
        j = i+1
        while j < N: 
            if sig_v(temperature[j]) != inc: break
            times = min(times, abs(temperature[j]) )
            j+=1

        times = min(times, abs(temperature[i]))
        for k in range(i+1,j):
           temperature[k] -= (inc*times)
        temperature[i] -= (inc*times)

    return cnt

N = len(adjust)
for i in range(N):
    cnt += adjust_temp(adjust, i, N)
    #print("cnt=",cnt,"  ", adjust)


print(cnt)

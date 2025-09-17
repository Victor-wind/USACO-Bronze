def estimated_range(traffic: list):
    n = len(traffic)
    # find the first 'none'/0, which is in traffic[0]
    for i in range(n):
        if traffic[i][0] == 0:
            break
    # start for index i to the end, find the best estimate
    low, high = (traffic[i][1], traffic[i][2])
    for k in range(i,n):
        if traffic[k][0] == 0:
            low = max(low, traffic[k][1])
            high = min(high, traffic[k][2])
        elif traffic[k][0] == 1: # on ramp
            low += traffic[k][1]
            high += traffic[k][2]
        else: # off ramp
            low -= traffic[k][2]
            high -= traffic[k][1]
        low = max(0, low)
        high = max(0, high)
        # print(f'{k=} {low=} {high=} \n')
    return (low, high) 


with open('traffic.in') as f:
    lines = f.readlines()

N = int(lines[0])
traffic = list()

for i in range(N):
    temp = list()
    words = lines[i+1].split()
    if words[0] == 'on':
        temp.append(1)
    elif words[0] == 'off':
        temp.append(-1)
    else:
        temp.append(0)
    temp.append(int(words[1]))
    temp.append(int(words[2]))
    traffic.append(temp)

last_mile_estimate = estimated_range(traffic)
print(last_mile_estimate)

# need to estimate the first mile speed reversedly
# to reuse the code/function, we can reverse traffic list and reverse off/on ramp
traffic.reverse()
traffic = [ [-x[0], x[1], x[2]] for x in traffic]
#print(traffic)

first_mile_estimate = estimated_range(traffic)
print(first_mile_estimate)

result = 1
with open('traffic.out','w') as f:
    f.write(f'{first_mile_estimate[0]} {first_mile_estimate[1]}\n')
    f.write(f'{last_mile_estimate[0]} {last_mile_estimate[1]}')

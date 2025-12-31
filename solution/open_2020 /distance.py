
with open('socdist1.in') as f:
    N = int(f.readline())
    cows = f.readline()
    cows = list(cows.strip())

print(N)
print(cows)        
result = 1

lead_zero = 0
end_zero = 0
idx = 0
dist_lst = list()


def add_second_cow(lead_zero, end_zero, dist_lst):
    # print(f'debug add_second_cow {lead_zero=} {end_zero=} {dist_lst=}')
    # add one cow to the beginning, if possible
    d1 = 0
    if lead_zero > 0: d1 = min(lead_zero, dist_lst[0])
    # or add one cow to the end, if possible
    d2 = 0
    if end_zero > 0: d2 = min(end_zero, dist_lst[0])
    # or add one cow in the middle : special case dist_lst = [1] or [] by above 2 cases
    d3 = min(dist_lst[-1]//2, dist_lst[0])
    # print(f'debug add_second_cow {d1=} {d2=} {d3=}')
    return max(d1, d2, d3)


def add_cow(lead_zero, end_zero, dist_lst):
    # add first cow to the beginning, if possible
    d1 = 0
    if lead_zero > 0:
        temp_lst = dist_lst[:]
        temp_lst.append(lead_zero)
        temp_lst.sort()
        d1 = add_second_cow(0, end_zero, temp_lst)
    # or add first cow to the end, if possible
    d2 = 0
    if end_zero > 0:
        temp_lst = dist_lst[:]
        temp_lst.append(end_zero)
        temp_lst.sort()
        d2 = add_second_cow(lead_zero, 0, temp_lst)
    # or add first cow in the middle, : special case dist_lst = [1] or [] by above 2 cases
    d3 = 0
    temp_lst = dist_lst[:]
    if dist_lst:
        k = dist_lst[-1]//2
        if dist_lst[-1] % 2 == 0:
            temp_lst.pop()
            temp_lst.append(k)
            temp_lst.append(k)
            temp_lst.sort()
            d3 = add_second_cow(lead_zero, end_zero, temp_lst)
        else:
            temp_lst.pop()
            temp_lst.append(k)
            temp_lst.append(k+1)
            temp_lst.sort()
            d3 = add_second_cow(lead_zero, end_zero, temp_lst)
    # print(f'debug add_cow {d1=} {d2=} {d3=}')
    return max(d1, d2, d3)


for i in range(N):
    if cows[i] == '1':
        lead_zero = i
        break

for i in range(N-1, -1, -1):
    if cows[i] == '1':
        end_zero = N-1-i
        break
print(lead_zero,end_zero)

idx = lead_zero
for i in range(lead_zero+1, N):
    if cows[i] == '1':
        dist_lst.append(i - idx)
        idx = i

dist_lst.sort()   
print(dist_lst)

# add two cows in the same dist element
result1 = 0
if dist_lst:
    largest = dist_lst[-1]
    result1 = largest//3

if cows == ['0'] * N:
    result2 = N - 1
else: # cows == "1000" or "00001" or "000100" and dist_lst = []
    result2 = add_cow(lead_zero,end_zero,dist_lst)


result = max(result1,result2)
print(result)
# special case of all '000000'
with open('socdist1.out', 'w') as f:
    f.write(f'{result}\n')

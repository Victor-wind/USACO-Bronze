N = int(input())
in_str = input().rstrip()
# find the numbers which do not include 'F', such as 'BB', 'EE'. It servers as an offset for final results
basic_cnt = 0
for i in range(1, N):
    if in_str[i] == 'E' and in_str[i - 1] == 'E':
        basic_cnt += 1
    if in_str[i] == 'B' and in_str[i - 1] == 'B':
        basic_cnt += 1
# var_cnt stores varying cnts for continuous 'F'
first_F, cnt_F = -1, 0
var_cnt = []
for i in range(N):
    if in_str[i] == 'F':
        cnt_F += 1
        if first_F == -1: first_F = i
    else:  # 'B' or 'E'
        if first_F != -1:
            if first_F == 0:
                # FB: (0, 1); FFB: (0,1,2); FFFB: (0,1,2,3)
                var_cnt.append((0, i - first_F, 1))
            else:
                if in_str[first_F - 1] == in_str[i]:
                    # BFB: (0, 2); BFFB: (1, 3); BFFFB: (0, 2, 4); BFFFFB: (1, 3, 5)
                    mx = i - first_F + 1
                else:
                    # BFE: (1); BFFE: (0, 2); BFFFE: (1,3); BFFFFE: (0,2,4)
                    mx = i - first_F
                mn = 0 if mx % 2 == 0 else 1
                var_cnt.append((mn, mx, 2))
            first_F = -1

# the last char is 'F'
if in_str[-1] == 'F':
    # BF: (0, 1); BFF: (0,1,2); BFFF: (0,1,2,3)
    mx = N - first_F
    # if all 'F'  FF: (0,1); FFF: (0,1,2)
    if mx == N:
        mx -= 1
    var_cnt.append((0, mx, 1))

# add all var_cnt together. (0,1,2) + {1,3} -> {1,2,3  3,4,5} = {1,2,3,4,5}
result = []
mx, mn, step = 0, 0, 2
#print(f'{basic_cnt=}')
for x in var_cnt:
    mn += x[0]
    mx += x[1]
    if x[2] == 1: step = 1
 #   print(f'{x=}')

answer = range(mn, mx+1, step)
print(len(answer))
for i in answer:
    print(basic_cnt+i)
    

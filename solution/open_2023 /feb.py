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
    
'''
N = int(input())
msg = input().rstrip()
#print(N)
#print(msg)

# The solution is based on dynamic programing
# range_prev_B is the possible min and max distinct excitement levels if ith msg is B
# range_prev_E is the possible min and max distinct excitement levels if ith msg is E
# At the index i, if msg[i] is 'B' or 'E', then range_prev_E/range_prev_B is None.
# range_prev_B[i] only depends on range_prev_B[i-1] and range_prev_E[i-1]
# if msg[i] == 'B', range_prev_E[i] is None, range_prev_B[i] = range_prev_B[i-1]+1 union range_prev_E[i-1]
# if msg[i] == 'F', range_prev_E and range_prev_B will Not be None
# For example msg = 'BFFFB'
#            range_prev_B   range_prev_E
#     B       [0,0]          None [99999999999999999999999999, -1]
#     F       [1,1]          [0,0]
#     F       [0,2] (0,2)    [1,1]  
#     F       [1,3] (1,3)    [0,2]  
#     B       [0,4] (0,2,4)  None
# the results will be range_prev_E[i-1] union range_prev_E[i-1]
# to speed up the execution, observe the steps in results is 1 (msg[0] == 'F' || msg[-1] == 'F') or 2. 
first_letter = msg[0]
range_prev_B = [99999999999999999999999999, -1]
range_prev_E = [99999999999999999999999999, -1]

if msg[0] == 'F':
    first_letter = 'BE'

for x in first_letter:
    if x == 'B':
       range_prev_B = [0,0]
    if x == 'E':
       range_prev_E = [0,0]

for i in range(1,len(msg)):
    c = msg[i]
    letters = list(c)
    if c == 'F':
        letters = list('BE')

    range_cur_B = [99999999999999999999999999, -1]
    range_cur_E = [99999999999999999999999999, -1]

    for letter in letters:
        mn, mx = 99999999999999999999999999, -1       
        if letter == 'B':
            mn = min(range_prev_B[0]+1, range_prev_E[0])
            mx = max(range_prev_B[1]+1, range_prev_E[1])
            range_cur_B[0] = mn 
            range_cur_B[1] = mx
        if letter == 'E':
            mn = min(range_prev_E[0]+1, range_prev_B[0])
            mx = max(range_prev_E[1]+1, range_prev_B[1])
            range_cur_E[0] = mn 
            range_cur_E[1] = mx
        
    range_prev_E[0] = range_cur_E[0]
    range_prev_E[1] = range_cur_E[1]
    range_prev_B[0] = range_cur_B[0]
    range_prev_B[1] = range_cur_B[1]
    #print(f'{c=} {range_prev_B=} {range_prev_E=}')    
    

mn_res = min(range_prev_E[0], range_prev_B[0]) 
mx_res = max(range_prev_E[1], range_prev_B[1])

step = 1 if msg[0] == 'F' or msg[-1] == 'F' else 2
result = range(mn_res, mx_res+1, step)

print(len(result))
for v in result:
    print(v)
'''

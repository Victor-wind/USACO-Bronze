# check whether n is a different number, it can be used to verify the calculation
def check_around(n):    
    n_lst = [int(i) for i in list(str(n))]
    if n_lst[0] != 4: return False
    for i in range(1, len(n_lst)):
        if n_lst[i] > 4: return True
        if n_lst[i] < 4: return False
    return False

nums_lst = [0] * 11
base_max = 49
base_min = 45
for i in range(2, 11):
    nums_lst[i] =  base_max-base_min+1
    base_max = base_max*10+9
    base_min = base_min*10-5   
# nums_lst stores differenct arounds numbers which have ith digits
# fo example, with 2 digits [45, ..., 49]; with 3 digits [445, ... 499];
# with 4 digits [4445,..., 4999]; with 5 digits [44445, ..., 49999];
#print(nums_lst)

nums_sum_lst = [0] * 11
for i in range(1, 11):
    nums_sum_lst[i] = nums_sum_lst[i-1]+nums_lst[i]
#print(nums_sum_lst)
    
T = int(input())

for _ in range(T):
    k_str = input().strip()
    k_int = int(k_str)
    # how many digits does k_int/k_str has?
    n = len(k_str)
    # differenct arounds numbers can be divided into 2 parts:
    # a: numbers < 9...9 {10^(n-1)-1}; b: numbers with exact n digits within [44..45 , ..., 49..9].
    a_cnt = nums_sum_lst[n-1]
    min_num = int('4'*n)+1
    max_num = int('4'+'9'*(n-1))
    k_int = min(max_num,k_int) 
    # rounds numbers of exact n digits are within [ min_num, min(min_num, k_int)]
    b_cnt = 0 if k_int < min_num else (k_int-min_num+1)
    #print(f'{k_int=} {k_str=} {min_num=} {a_cnt=} {b_cnt=} {a_cnt+b_cnt}')
    print(a_cnt+b_cnt)

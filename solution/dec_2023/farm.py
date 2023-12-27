import math
def sort_return_index(lst):
    # Use sorted() with enumerate() to get a sorted list of (index, value) pairs
    sorted_indices = sorted(enumerate(lst), key=lambda x: (x[1], -x[0]))
    sorted_indices = [index for index, value in sorted_indices]
    return sorted_indices

def find_days(N, h, a, t):
    goal_index = sort_return_index(t)
    # height of plant goal_index[i] should > height of plant goal_index[i+1] at the final state
    # only need to check neighbor index as if h[i] > h[i+1] and h[i+1] > h[i+2] => h[i] > h[i+2]
    days_needed = 0
    for i in range(N-1):
        h1, h2 = h[goal_index[i]],h[goal_index[i+1]] 
        a1, a2 = a[goal_index[i]],a[goal_index[i+1]]
        # calculate how many days needs for h[goal_index[i]] > h[goal_index[i+1]]
        # there are 4 cases: a. h1 < h2 && a1 > a2;b h1 < h2 && a1 <= a2;c h1 > h2 && a1 > a2;d h1 > h2 && a1 <= a2;
        # for a, days needed for h1 > h2 are (h2-h1)//(a1-a2)+1
        # for b, it could not, no matter how many days pass
        # for c, always h1 > h2
        # for d, h1 > h2 at the beginning, but afer some days, h1 maybe <= h2 
        if h1 < h2 and a1 > a2:
            days = (h2-h1)//(a1-a2)+1
            days_needed = max(days_needed, days)

    # after days_needed, we are sure h[i] > h[i+1], if original h[i] < h[i+1]
    # but we also need to check cases b and d.
    for i in range(N):
        h[i] += a[i]*days_needed

    for i in range(N-1):
        h1, h2 = h[goal_index[i]],h[goal_index[i+1]]
        if h1 <= h2: return -1
    '''
    time out for test cases 9 -13 O(N^2)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if h[j] > h[i]: cnt += 1
        if cnt != t[i]: return -1        
    '''
    return days_needed

T = int(input())

for _ in range(T):
    N = int(input())
    h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]    
    #print(f'{N=}')
    #print(f'   {h=}')
    #print(f'   {a=}')
    #print(f'   {t=}')
    print(find_days(N, h, a, t))
 

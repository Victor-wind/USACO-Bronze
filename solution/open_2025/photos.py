T = int(input())
#print(T)

def max_cows(N, heights):
    heights.sort()
    nums_lst = list()
    cur_height = heights[N-1]
    cnt = 1
    for i in range(N-2, -1, -1):
        if heights[i] == cur_height:
            cnt += 1
        else:
            nums_lst.append(cnt)
            cnt = 1
            cur_height = heights[i]
    #Add the last one
    nums_lst.append(cnt)
    #print(f'debug {heights=} {nums_lst=}')
    # calculate the max cows in the photo, start from the middle
    # h_i is the highest, and must be 1
    cow_cnt = 1
    # must h_k >= 2, expanding from the middle, add 2 each loop
    for i in range(1, len(nums_lst)):
        if nums_lst[i] >=2:
            cow_cnt += 2
    return cow_cnt

for _ in range(T):
    N = int(input())
    heights = [int(x) for x in input().split()]
    print(max_cows(N, heights))

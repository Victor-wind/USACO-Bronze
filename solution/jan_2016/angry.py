with open('angry.in') as f:
    lines = f.readlines()

N = int(lines[0])

points = [ int(v) for v in lines[1:N+1]]
points.sort()
print(f'{points}')

def search_left(points, i):
    cnt = 0
    radius = 1
    left_bound = points[i] 
    while i >= 0:
        j = i
        while i >=0 and points[i] >= left_bound:
            cnt += 1
            new_bound = points[i]-radius
            i -=1
        left_bound = new_bound
        radius +=1
        if j == i:
            break
    return cnt
    
def search_right(points, i):
    cnt = 0
    radius = 1
    right_bound = points[i]
    N = len(points)
    while i < N:
        j = i
        while i < N and points[i] <= right_bound:
            cnt += 1
            new_bound = points[i] + radius
            i +=1
        right_bound = new_bound
        radius +=1
        if j == i:
            break
    return cnt

max_cnt = 0

for i in range(len(points)):
    # search left and right
    cnt = search_left(points, i) + search_right(points, i) - 1
    max_cnt = max(max_cnt, cnt)
    # print(f'{i=} {cnt=}')


with open('angry.out', 'w') as f:
    f.write(f'{max_cnt}\n')
    

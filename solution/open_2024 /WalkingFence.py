# https://usaco.org/current/data/sol_prob2_bronze_open24.html has a simpler solution
# using the assumption 0≤x,y≤1000; but below is more general
def distance(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y1-y2)
    if y1 == y2:
        return abs(x1-x2)
    return -1;

def build_map(m_x, m_y, p1, p2, i):
    if p1[0] == p2[0]:
        range_y = (p1[1], p2[1], i) if p1[1] < p2[1] else (p2[1], p1[1], i) 
        if p1[0] in m_x:
            m_x[p1[0]].append(range_y)            
        else:
            m_x[p1[0]] = [range_y]
    if p1[1] == p2[1]:
        range_x = (p1[0], p2[0], i) if p1[0] < p2[0] else (p2[0], p1[0], i)
        if p1[1] in m_y:
            m_y[p1[1]].append(range_x)
        else:
            m_y[p1[1]] = [range_x]

def binary_find_post(x, y, map_x, map_y): # linear search times out
    if x in map_x:
        lst = map_x[x]; left = 0; right = len(lst)-1
        while left <= right:
            middle = (left+right)//2
            y1, y2, post = lst[middle]
            if y1<= y <= y2: return post
            elif y > y2: left = middle+1
            else: right = middle-1
    if y in map_y:
        lst = map_y[y]; left = 0; right = len(lst)-1
        while left <= right:
            middle = (left+right)//2
            x1, x2, post = lst[middle]
            if x1<= x <= x2: return post
            elif x > x2: left = middle+1
            else: right = middle-1                        
    return None

def find_walk_distance(x1,y1, x2,y2):
    # need to use binary search to find posts, otherwise timeout
    p1 = binary_find_post(x1,y1,map_x, map_y)
    p2 = binary_find_post(x2,y2,map_x, map_y)
    if p1 is not None and p2 is not None:
        # to simplify the calculation, make p2 after p1 along the paths
        # swap p1/p2 (x1,y1)/(x2,y2)
        if distances[p1] > distances[p2]: 
            p1, p2 = p2, p1
            x1, x2 = x2, x1
            y1, y2 = y2, y1
    else:
        return -1
    # distance between (x1,y1) and (x2,y2) is distance of p1,p2 + (x1,y1)->p1 - (x1,y1)->p1
    ret_v = distances[p2]-distances[p1]
    ret_v += distance(x1,y1, posts[p1][0],posts[p1][1])
    ret_v -= distance(x2,y2, posts[p2][0],posts[p2][1])
    if p1 == p2: #unknown which one is first (x1,y1) vs (x2,y2) 
        ret_v = distance(x1,y1,x2,y2)
    return min(ret_v, distances[0]-ret_v)

N, P = [int(x) for x in input().split()]
posts = list()
for _ in range(P):    
    posts.append([int(x) for x in input().split()])
cows = list()
for _ in range(N):
    cows.append([int(x) for x in input().split()])

# distances from post 0 to post k
distances = [0] * P
for i in range(P-1):
    distances[i+1] += distances[i]
    k = distance(posts[i][0], posts[i][1], posts[i+1][0], posts[i+1][1])
    distances[i+1] += k
distances[0] = distances[P-1]+distance(posts[0][0], posts[0][1], posts[P-1][0], posts[P-1][1]) 

# build map based on x, y
map_x = dict()
map_y = dict()
for i in range(0,P):
    build_map(map_x, map_y, posts[i], posts[i-1], i)

for cow in cows:
    dist = find_walk_distance(cow[0], cow[1], cow[2], cow[3])
    print(dist)

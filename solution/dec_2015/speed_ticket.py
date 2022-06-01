with open('speeding.in') as f:
    lines = f.readlines()

input_lines = [line.split() for line in lines]
input_num = [  [int(v) for v in line]  for line in input_lines]

N, M = input_num[0][0], input_num[0][1]
road_segs = input_num[1:1+N]
Bessie_journey = input_num[1+N:]

print(f'road_segs  = {road_segs}')
print(f'Bessie_journey = {Bessie_journey}')

max_over_speed = 0

i, j = 0,0
cur_road = road_segs[i][0]
drive_road = Bessie_journey[j][0]

while i < N:

    print(f' i = {i} j = {j}')

    # calculate over_speed 
    max_over_speed = max(max_over_speed, (Bessie_journey[j][1]-road_segs[i][1]) )

    if cur_road == drive_road:
        i +=1; j +=1
        if i < N: cur_road = road_segs[i][0]
        if j < M: drive_road = Bessie_journey[j][0]
    elif cur_road > drive_road:
        cur_road -= drive_road 
        j+=1
        if j < M: drive_road = Bessie_journey[j][0]
    else:  # cur_road < drive_road
        drive_road -= cur_road
        i+=1
        if i < N: cur_road = road_segs[i][0]

print(max_over_speed)

with open('speeding.out','w') as f:
     f.write(str(max_over_speed))
     

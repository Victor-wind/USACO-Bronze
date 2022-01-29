N = int(input())

cell_set = set()
lucky_cows = set()

def check_neighbor(cell_set, cell):
    left  = (cell[0]-1, cell[1])
    right = (cell[0]+1, cell[1])
    top   = (cell[0], cell[1]+1)
    bottom= (cell[0], cell[1]-1)
    neighbor = 0
    if left in cell_set:
        neighbor +=1
    if right in cell_set:
        neighbor +=1
    if top in cell_set:
        neighbor +=1
    if bottom in cell_set:
        neighbor +=1
    return neighbor


comfortable_cows = 0

for i in range(N):
    s = input()
    cell_str = s.split()
    cow = [int(c) for c in cell_str]
    cow = tuple(cow)
    cell_set.add(cow)

    n = check_neighbor(cell_set, cow)
    if n == 3:
        lucky_cows.add(cow)
        comfortable_cows += 1
        
    left_cow = (cow[0]-1, cow[1])
    right_cow = (cow[0]+1, cow[1])
    above_cow = (cow[0], cow[1]+1)
    below_cow = (cow[0], cow[1]-1)

    if left_cow in cell_set and left_cow not in lucky_cows and check_neighbor(cell_set, left_cow) == 3:
        comfortable_cows += 1
        lucky_cows.add(left_cow)
    if left_cow in lucky_cows and check_neighbor(cell_set, left_cow) != 3:
        comfortable_cows -= 1
        lucky_cows.remove(left_cow)

    if right_cow in cell_set and right_cow not in lucky_cows and check_neighbor(cell_set, right_cow) == 3:
        comfortable_cows += 1
        lucky_cows.add(right_cow)
    if right_cow in lucky_cows and check_neighbor(cell_set, right_cow) != 3:
        comfortable_cows -= 1
        lucky_cows.remove(right_cow)

    if above_cow in cell_set and above_cow not in lucky_cows and check_neighbor(cell_set, above_cow) == 3:
        comfortable_cows += 1
        lucky_cows.add(above_cow)
    if above_cow in lucky_cows and check_neighbor(cell_set, above_cow) != 3:
        comfortable_cows -= 1
        lucky_cows.remove(above_cow)

    if below_cow in cell_set and below_cow not in lucky_cows and check_neighbor(cell_set, below_cow) == 3:
        comfortable_cows += 1
        lucky_cows.add(below_cow)
    if below_cow in lucky_cows and check_neighbor(cell_set, below_cow) != 3:
        comfortable_cows -= 1
        lucky_cows.remove(below_cow)
        
    print(comfortable_cows)
    


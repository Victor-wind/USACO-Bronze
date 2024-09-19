def MinBags(hunger_level):
    #print(hunger_level)
    bags = 0
    N = len(hunger_level)
    if N <= 1:
        print(0); return

    # special cases, make processing more efficient
    min_level = min(hunger_level)
    if hunger_level[0] > min_level:
        corns = hunger_level[0] - min_level
        bags += corns + corns
        hunger_level[0] -= corns
        hunger_level[1] -= corns
    if hunger_level[-1] > min_level:
        corns = hunger_level[-1] - min_level
        bags += corns + corns
        hunger_level[-1] -= corns
        hunger_level[-2] -= corns
            
    # if hunger_level[i+1] > hunger_level[i], the only choice is to bring  hunger_level[i+1] and  hunger_level[i+2] down
    # similar for hunger_level[i] > hunger_level[i+1]
    equal = True
    while hunger_level[0] <= hunger_level[1] and hunger_level[-1] <= hunger_level[-2] and hunger_level[0] >= 0:
        equal = True
        # from left to right
        for i in range(1, N-1, 1):
            if hunger_level[i] > hunger_level[i-1]:
                corns = hunger_level[i] - hunger_level[i-1]
                bags += corns + corns
                hunger_level[i+1] -= corns
                hunger_level[i] -= corns                
                equal = False
        # from right to left
        for i in range(N-2, 0, -1):
            if hunger_level[i] > hunger_level[i+1]:
                corns = hunger_level[i] - hunger_level[i+1]
                bags += corns + corns
                hunger_level[i] -= corns
                hunger_level[i-1] -= corns
                equal = False
        if equal == True:
            #print(f'debug equal  {hunger_level=}')
            break
        
    if hunger_level[0] > hunger_level[1] or hunger_level[-1] > hunger_level[-2] or hunger_level[0] < 0:
        #print(f'debug {hunger_level=}')
        print(-1)
    else:
        print(bags)
    return

T = int(input())
for _ in range(T):
    N = int(input())
    hunger_level = [ int(x) for x in input().split()]
    MinBags(hunger_level)

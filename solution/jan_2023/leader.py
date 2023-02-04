import sys

N = int(input())
cows = input()
cows_l = [int(x)-1 for x in input().split()]

def first_cow(cows: str, c: str):
    for i,v in enumerate(cows):
        if v == c:
            return i
    return -1

def last_cow(cows: str, c: str):
    n = len(cows)-1
    for i in range(n, -1, -1):
        if cows[i] == c:
            return i
    return -1

first_H = first_cow(cows, 'H')
first_G = first_cow(cows, 'G')
last_H  = last_cow(cows, 'H')
last_G  = last_cow(cows, 'G')

# print(f'{first_H=} {first_G=} {last_H=} {last_G=}')

def find_pairs():
    pairs = 0
    if cows[0] == 'G':
        # lead must be the first_H : if the lead is Not the first_H - > lead H must contain lead G 
        # -> lead G is after lead H -> it is NOT possible: a. lead G cann't contain lead H (position is after H)
        # b. lead G cann't contain all the cows of breed G (the first cow is G)
        if cows_l[first_H] < last_H:
            return 0
        # loop through cows for how many G could pair with first_H 
        for i in range(first_H):
            if cows_l[i] >= first_H or ( i == first_G and cows_l[i] >= last_G ):
                pairs += 1
    else: # 'H'
        # the same logic above
        if cows_l[first_G] < last_G:
            return 0
        for i in range(first_G):
            if cows_l[i] >= first_G or ( i == first_H and cows_l[i] >= last_H):
                pairs += 1
    return pairs
                
print(find_pairs())

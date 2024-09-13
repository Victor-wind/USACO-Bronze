import itertools

def comp_dices(dicesA, dicesB):
    greaterCnt = [ j>i for j in dicesA for i in dicesB ]
    lessCnt = [ i>j for j in dicesA for i in dicesB ]
    return sum(greaterCnt) - sum(lessCnt)
    

def dices_exist():
    # itertools.product has worse performace than 4 for loops
    dices_range = range(1,11)
    dices_Cs = list(itertools.product(dices_range, repeat=4))
    for dices_C in dices_Cs:
        if comp_dices(dices_B, dices_C) > 0 and comp_dices(dices_C, dices_A) > 0:
            print("yes")
            return
    print("no")
    

T = int(input())

for i in range(T):
    dices = [int(x) for x in input().split()]
    dices_A = dices[0:4]
    dices_B = dices[4::]
    # print(f'{dices_A=} {dices_B=}')
    # this solution is better than the offical solution, as it does fewer comparision
    # https://usaco.org/current/data/sol_prob2_bronze_jan22.html
    if comp_dices(dices_A, dices_B) == 0:
        print("no")
        continue

    if comp_dices(dices_A, dices_B) < 0:
        dices_A, dices_B = dices_B, dices_A

    dices_exist()

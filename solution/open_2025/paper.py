N, M = [ int(x) for x in input().split()]
lose_to = dict()

lose_to = { i: [] for i in range(N)}

#print(lose_to)

def game_win(s1, s2):
    # Bessie needs to win against Elsie, no matter what Elsie puts
    # So Bessie needs to have a symbol that wins BOTH Elsie's symbols  
    set_1 = set(lose_to[s1])
    set_2 = set(lose_to[s2])
    set_win = set_1 & set_2
    #print(f' {s1} {s2} {set_win}')
    s = len(set_win)
    res = 0
    if s != 0:
        # math problem: for a symbol k, the combination is (k, s_1),(k, s_2),.. (k,s_n);
        # (s_1, k),(s_2, k),.. (s_n,k). There are some duplicates (k,k), (k,k),
        # (k,a), (a,k), (k,a), (a,k) for another a in set_win. For each k in set_win,
        # subtract len(set_win)
        res = (N+N-s)*s
    return res

for i in range(N):
    symbols = input()
    n = len(symbols)
    for j in range(n):
        if symbols[j] == 'W': # symbol i wins against symbol j
            lose_to[j].append(i)
        elif symbols[j] == 'L': # symbol i loses against symbol j
            lose_to[i].append(j)

#print(lose_to)

for _ in range(M):
    s1, s2 = [ int(x)-1 for x in input().split()]
    print(game_win(s1,s2))

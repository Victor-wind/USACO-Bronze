'''
1. if T is [1, 9], Bessie removes T stones; Elsie has no stones. Bessie wins.
2. if T is 10, Bessie could not removes 10 stones as 10 is not palindromes number; No matter what K stones Bessie removes, Elsie removes the remaining 10-K stones. Elsie wins.
3. if T is in [11, 19], Bessie removes T%10 stones, leaving 10 stones to Elsie; as in case 2, Elsie could not win.  Bessie wins.
4. if T is 20, Bessie could not removes 10 or 20 stones as 10 / 20 is not palindromes number; No matter what K stones Bessie removes, Elsie takes 10-K%10 stones, leaving Bessie 10*N stones. Elsie wins.
...
this process continues, it concludes that anyone who has 10*N stones first loses, the other wins. 
'''
T = int(input())
for _ in range(T):
    s = int(input())
    print('B' if s % 10 else 'E')
    

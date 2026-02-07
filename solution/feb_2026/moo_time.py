import sys

T, k = [int(x) for x in sys.stdin.readline().split()]
#print(T, k)

letter_flipped = { 'M': 'O', 'O': 'M'}
def flip_letter(letter, n):
    if n & 1 == 0:
        return letter
    else:
        return letter_flipped[letter]
          

def favorite_moo(n, k, letters):
    # print(letters)
    result = [''] * n
    j = 0
    for i in range(n-1, -1, -1):
        c = letters[i]
        result[i] = flip_letter(c,j)
        if result[i] == 'O':
            j += 1
    sys.stdout.write('YES\n')
    if k == 1:
        out_str = ''.join(result)
        sys.stdout.write(f'{out_str}\n')
        
    
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    letters = sys.stdin.readline().strip()
    favorite_moo(N, k, letters)
    


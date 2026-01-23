import sys

# The official solution is clearly explained 

def split_letters(N, letters):
    if N & 1:
        sys.stdout.write('-1'+'\n')
        return

    result = [1] * (3*N)
    half_size = 3*N//2
    if letters[:half_size] == letters[half_size:]:
        sys.stdout.write('1' + '\n')
        stdout_output = ' '.join([str(i) for i in result])
        sys.stdout.write(stdout_output)
        sys.stdout.write('\n')
        return

    # split letters into half letters[:half_size] and half_size[half_size:]
    # get 3-letter pairs from each half and compare them,
    j = 0
    k = half_size
    for i in range(N//2):
        first_letter_1 = letters[j]
        first_letter_2 = letters[k]
        third_letter_2 = letters[k+2]
        # consider the possible words: COW OWC WCO COW
        if first_letter_1 == third_letter_2:
            result[j] = result[k+2] = 2
        elif first_letter_1 == first_letter_2:
            pass
        else:
            result[j+2] = result[k] = 2
        j += 3
        k += 3
    sys.stdout.write('2' + '\n')
    stdout_output = ' '.join([str(i) for i in result])
    sys.stdout.write(stdout_output)
    sys.stdout.write('\n')


T, K = [int(x) for x in sys.stdin.readline().split()]
for _ in range(T):
    N = int(sys.stdin.readline())
    letters = sys.stdin.readline().strip()
    split_letters(N, letters)


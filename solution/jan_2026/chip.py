import sys

T = int(sys.stdin.readline().strip())
test_cases = [ [int(x) for x in sys.stdin.readline().split()] for _ in range(T)]
# print(test_cases)

def solution(case):
    A, B, ca, cb, f = case
    result = 0
    # print(A, B, ca, cb, f)
    # convert B to A based on cb/ca, no matter what
    k = B // cb
    A += k * ca
    B = B - k*cb
    #print(A, B, f)
    if A >= f:
        return 0
    a_needed = f - A
    if ca >= cb: # give Bessie (a_needed -1) chip A directly
        result = + (a_needed -1)
        A = f - 1
    else: # give Bessie chip B, then Bessie converts B to A
        k = a_needed // ca
        if (k * ca) == a_needed:
            k -= 1
        result = + (k * cb)
        A += k*ca
    # give Bessie chip A & B as much as possible
    a_needed = f - A - 1
    result += a_needed
    b_needed = cb - B - 1 # don't trigger convertion 
    result += b_needed
    result += 1
    return result

for case in test_cases:
    print(solution(case))

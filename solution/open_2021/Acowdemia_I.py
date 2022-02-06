
N, L = input().split()

N = int(N)
L = int(L)
#print(N, L)


s_list = input().split()
citations = [ int(s) for s in s_list]


def findHIndex(citations):
    citations.sort(reverse=True)
    N = len(citations)
    res = N
    for i in range(N):
        if citations[i]<i+1:
            res = i
            break
    return res

k = findHIndex(citations)

while L > 0 and k>=0:
    citations[k] += 1
    L -= 1
    k -= 1

k = findHIndex(citations)
print(k)

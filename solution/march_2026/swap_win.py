# All tests pass with 2400 MS

import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    out = []

    for _ in range(T):
        N, M = map(int, input().split())

        t = bytearray(input().strip(), 'ascii')
        s = [bytearray(input().strip(), 'ascii') for _ in range(N)]

        row0 = s[0]
        steps = []

        # Phase 1: perfect swaps inside row0
        for i in range(M):
            if row0[i] != t[i]:
                for j in range(i+1, M):
                    if row0[j] == t[i] and row0[i] == t[j]:
                        row0[i], row0[j] = row0[j], row0[i]
                        steps.append((1,1,i+1,j+1))
                        break

        # Phase 2: partial swaps inside row0
        for i in range(M):
            if row0[i] != t[i]:
                for j in range(M):
                    if row0[j] == t[i] and row0[j] != t[j]:
                        row0[i], row0[j] = row0[j], row0[i]
                        steps.append((1,1,i+1,j+1))
                        break

        # Phase 3: vertical swaps
        for i in range(M):
            if row0[i] != t[i]:
                for r in range(1, N):
                    if s[r][i] == t[i]:
                        row0[i], s[r][i] = s[r][i], row0[i]
                        steps.append((2,1,r+1,i+1))
                        break

        # Phase 4: general fixes
        pos = [[] for _ in range(26)]

        for r in range(1, N):
            for c in range(M):
                pos[s[r][c]-97].append((r,c))

        for i in range(M):
            if row0[i] == t[i]:
                continue

            idx = t[i]-97

            while pos[idx]:
                r,c = pos[idx].pop()

                if s[r][c] != t[i]:
                    continue

                # horizontal swap inside row r. after swap, the original pos is not valid. 
                # That is the reason to check 'if s[r][c] != t[i]'
                if c != i:
                    pos[s[r][i]-97].append((r,c))
                    s[r][c], s[r][i] = s[r][i], s[r][c]
                    steps.append((1,r+1,c+1,i+1))

                # vertical swap
                row0[i], s[r][i] = s[r][i], row0[i]
                steps.append((2,1,r+1,i+1))
                break

        out.append(str(len(steps)))
        for a,b,c,d in steps:
            out.append(f"{a} {b} {c} {d}")           
            

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()

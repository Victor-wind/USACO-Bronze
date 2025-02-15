T = int(input())


def solution():
    N, A, B = [int(x) for x in input().split()]
    photo = list()
    for _ in range(N): photo.append(input())
    # print(photo)
    ori_photo = [[-1] * N for _ in range(N)]
    star_cnt = 0

    for i in range(N):
        for j in range(N):
            if photo[i][j] == 'W':  # if 'W', the * can disappear
                ori_photo[i][j] = 0

            if photo[i][j] == 'B':  # both original and shifted photo need to be *
                ori_photo[i][j] = 1
                star_cnt += 1
                if i < B or j < A:  # not possible for * to shift from [i-B][j-A] to [i][j]
                    return -1
                if ori_photo[i - B][j - A] == 0:  # could not shift * from [i-B][j-A]
                    return -1
                elif ori_photo[i - B][j - A] == -1:  # undecided before, now we know it must be *
                    ori_photo[i - B][j - A] = 1
                    star_cnt += 1
                else:
                    pass  # ori_photo[i - B][j - A] == 1:

            if photo[i][j] == 'G':
                if i < B or j < A:  # not shift * from [i-B][j-A] to [i][j]
                    ori_photo[i][j] = 1
                    star_cnt += 1
                else:
                    if ori_photo[i - B][j - A] == 1:  # may shift  * from [i-B][j-A] to [i][j]
                        # * at [i][j] may from [i-B][j-A];
                        # however, it is also possible [i][j] has *, then disappear in shifted photo
                        ori_photo[i][j] = -1
                    else:
                        ori_photo[i][j] = 1
                        star_cnt += 1
    # print(ori_photo)
    return star_cnt


for _ in range(T):
    cnt = solution()
    print(cnt)

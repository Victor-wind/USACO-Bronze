with open('tttt.in') as f:
    lines = f.readlines()

def tic_win_1(l_char):
    if l_char[0] == l_char[1] and l_char[0] == l_char[2]:
        return True
    return False


def tic_win_2(l_char):
    if tic_win_1(l_char):
        return False
    l_char.sort()

    if l_char[0] == l_char[1] or l_char[1] == l_char[2]:
        return True

    return False


cnt_win_1 = 0
cnt_win_2 = 0

input_list = [ [lines[0][0], lines[0][1], lines[0][2]],
               [lines[1][0], lines[1][1], lines[1][2]],
               [lines[2][0], lines[2][1], lines[2][2]],
               [lines[0][0], lines[1][0], lines[2][0]],
               [lines[0][1], lines[1][1], lines[2][1]],
               [lines[0][2], lines[1][2], lines[2][2]],
               [lines[0][0], lines[1][1], lines[2][2]],
               [lines[0][2], lines[1][1], lines[2][0]]]

print(input_list)

win_1_set = set()
win_2_set = set()

for l in input_list:
    l.sort()
    if tic_win_1(l):
        for c in l:
            win_1_set.add(c)
    if tic_win_2(l):
        if l[0] == l[1]:
            win_2_set.add((l[0], l[2]))
        else:
            win_2_set.add((l[0], l[1]))
               

print(len(win_1_set))
print(win_1_set)
print(len(win_2_set))
print(win_2_set)

with open('tttt.out','w') as f:
     f.write(f'{len(win_1_set)}\n')
     f.write(f'{len(win_2_set)}\n')
   

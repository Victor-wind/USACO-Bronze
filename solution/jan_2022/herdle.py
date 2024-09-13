answer = ''
guess = ''
for i in range(3):
    x = input()[0:3]
    answer += x
#print(f'{answer=}')
for i in range(3):
    x = input()[0:3]
    guess += x
#print(f'{guess=}')

green_cnt = 0
yellow_cnt = 0
answer_dic = dict()
guess_dic = dict()

for i in range(9):
    if answer[i] == guess[i]:
        green_cnt += 1
    else:
        answer_dic[answer[i]] = answer_dic.get(answer[i],0) + 1
        guess_dic[guess[i]] = guess_dic.get(guess[i],0)+1

for k, v in guess_dic.items():
    answer_v = answer_dic.get(k,0)
    yellow_cnt += min(v,answer_v)

print(green_cnt)
print(yellow_cnt)

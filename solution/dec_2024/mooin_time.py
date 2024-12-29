import string
ascii_letters = string.ascii_lowercase

N,F = [int(i) for i in input().split()]
letters = input().strip()
#print(letters)
moo_dic = dict()
for i in range(N-2):
    moo = letters[i:i+3]
    if moo[1] == moo[2] and moo[0] != moo[1]:
        moo_dic[moo] = moo_dic.get(moo,0)+1

result_set = set()
for k,v in moo_dic.items():
    if v >= F:
        result_set.add(k)


def process_words(moo_dic, moo, F, adjust):
    moo_dic[moo] = moo_dic.get(moo,0) + adjust
    # eveh if adjust == -1, does not matter to update result_set
    if moo_dic[moo] >= F:
        result_set.add(moo)        
    return


def update_dict(letters, i, adjust, b):
    moos = list()
    # if adjust == 1, add 1 to dict values; otherwise substract 1
    if (i+2) < N and letters[i+1] == letters[i+2] != b:
        moo = b + letters[i+1] + letters[i+2]
        moos.append(moo)        
    if i > 0 and (i+1) < N and b == letters[i+1] != letters[i-1]:
        moo = letters[i-1] + b + letters[i+1]
        moos.append(moo)        
    if i > 1 and letters[i-1] == b != letters[i-2]:
        moo = letters[i-2] + letters[i-1] + b
        moos.append(moo)
    # the order to process moo does not matter. We know moo from ABO, AOB, OAB cann't be the same.
    for moo in moos:
        process_words(moo_dic, moo, F, adjust)
    return


for i in range(N):
    # replace a letter from ascii_letters, need to removed them, then add back at the end of the loop
    # example:  vovoo. When replacing second 'v' with 'o', moo_dic adds 'voo', but also needs to remove the original 'voo'
    update_dict(letters, i, -1, letters[i])
    for t in ascii_letters:
        update_dict(letters, i, 1, t)
        # restore moo_dic
        update_dict(letters, i, -1, t)       
    update_dict(letters, i, 1, letters[i])
            
result_list = list(result_set)
result_list.sort()
print(len(result_list))
for w in result_list:
    print(w)
 

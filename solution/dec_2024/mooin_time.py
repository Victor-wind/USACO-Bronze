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
#print(moo_dic)

result_set = set()
for k,v in moo_dic.items():
    if v >= F:
        result_set.add(k)

def process_words(moo_dic, moo, F, result_set):
    cnt = moo_dic.get(moo,0)
    if (cnt+1)>=F:
        result_set.add(moo)        
    return
    
for i in range(N):
    # replace a letter from ascii_letters
    replaced = [None]*3
    if (i+2) < N and letters[i+1] == letters[i+2] and letters[i] != letters[i+1]:
        replaced[0] = letters[i]+letters[i+1]+letters[i+2]
        moo_dic[replaced[0]] -= 1
    if i > 0 and (i+1) < N and letters[i] == letters[i+1] and letters[i-1] != letters[i]:
        replaced[1] = letters[i-1]+letters[i]+letters[i+1]
        moo_dic[replaced[1]] -= 1
    if i > 1 and letters[i-1] == letters[i] and letters[i-2] != letters[i-1]:
        replaced[2] = letters[i-2]+letters[i-1]+letters[i]
        moo_dic[replaced[2]] -= 1
    
    for t in ascii_letters:
        if t == letters[i]: continue        
        if (i+2)<N and letters[i+1]==letters[i+2] and t!=letters[i+1]:
            moo = t + letters[i+1] + letters[i+2]
            process_words(moo_dic, moo, F, result_set)
        if i>0 and (i+1)<N and t == letters[i+1] and t!=letters[i-1]:
            moo = letters[i-1] + t + letters[i+1]
            process_words(moo_dic, moo, F, result_set)
        if i>1 and letters[i-2]!=letters[i-1] and t==letters[i-1]:
            moo = letters[i-2] + letters[i-1] + t
            process_words(moo_dic, moo, F, result_set)
            
    for m in replaced:
        if m:
            moo_dic[m] = moo_dic.get(m,0)+1
            
result_list = list(result_set)
result_list.sort()
print(len(result_list))
for w in result_list:
    print(w)

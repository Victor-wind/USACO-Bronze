n = int(input())
photo = input()

reverse_cnt = 0

'''
10 HGHGHGGHGH ->2
8 HGGHGHHG  -> 2
10 HGGHHGGHHG ->
'''
i = 0
last = 0
cur = 0
list_sign = []
while i < n:
    if photo[i] == 'H' and photo[i+1] == 'H':
        pass
    elif photo[i] == 'G' and photo[i+1] == 'G':
        pass
    elif photo[i] == 'H' and photo[i+1] == 'G':
        if last == 1 or last == 0: cur += 1; last = 1
        else: # last == -1
            list_sign.append(cur)
            last, cur = 1, 1            
    elif photo[i] == 'G' and photo[i+1] == 'H':
        if last == -1 or last == 0: cur -= 1; last = -1
        else: # last == 1
            list_sign.append(cur)
            last, cur = -1, -1
    i+=2
   
list_sign.append(cur)

if list_sign[-1] > 0:
    list_sign.pop()

'''
After processing, the list_sign will be like [1 -1 1 -1 ... -1 ] or [-1 1 -1 .. -1]
[1 -1 1 -1 ... -1 ] -> [-1 -1 1 -1 ... -1 ] -> [1 1 1 -1 ... -1 ] -> [-1 -1 -1 -1 ... -1 ]
... -> [-1 -1 -1 -1 ... -1 ] -> [1 1 1 1 ... 1 ] 

'''
print(len(list_sign))

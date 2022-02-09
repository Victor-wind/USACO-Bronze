
with open('whereami.in') as f:
    lines = f.readlines()

mail_box  = lines[1]

def unique_str(mail_box):
    n = len(mail_box)
    search_set = set()
    res = n
    
    for k in range(1,n):
        search_set.clear()
        for i in range(0, n-k+1):
            t = mail_box[i: i+k]
            #print(t)
            if t in search_set:
                break;
            search_set.add(t)
        
        if i+1 == len(search_set) and i == n-k:
            res = k
            #print('i==',i)
            return k

    return res

res = unique_str(mail_box)
with open('whereami.out', 'w') as f:
    f.write(str(res))
    

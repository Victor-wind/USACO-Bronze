with open('whereami.in') as f:
    lines = f.readlines()

N = int(lines[0])
mail_box  = lines[1].strip()[0:N]
print(mail_box)

def check_value(mail_box, k):
    n = len(mail_box)
    boxes_k = set()
    for i in range(k-1,n):
        sub_str = mail_box[i-k+1:i+1]
        if sub_str in boxes_k:
            return False
        else:
            boxes_k.add(sub_str)
    return True

result = N
for k in range(1, N):
    if check_value(mail_box, k):
        result = k
        break

print(result)
with open('whereami.out', 'w') as f:
    f.write(str(result))   

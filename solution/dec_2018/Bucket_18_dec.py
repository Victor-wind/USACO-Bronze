with open('blist.in') as f:
    lines = f.readlines()

N = int(lines[0])
cow_times = list()
cow_bucket = dict()
for i in range(N):
   cow = [int(i) for i in lines[i+1].split()]
   # print(cow)
   cow_times.append(cow[0])
   cow_times.append(cow[1])
   cow_bucket[cow[0]] = cow_bucket.get(cow[0],0) + cow[2]
   cow_bucket[cow[1]] = cow_bucket.get(cow[1],0) - cow[2]

cow_times.sort()
#print(cow_times)
#print(cow_bucket)

max_bucket = 0
cur_bucket = 0
for i in cow_times:
    cur_bucket += cow_bucket[i]
    max_bucket = max(max_bucket, cur_bucket)

print(max_bucket)
with open('blist.out','w') as f:
     f.write(str(max_bucket))
    

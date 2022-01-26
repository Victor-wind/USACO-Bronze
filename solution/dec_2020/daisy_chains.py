n = input()
N = int(n)

petals = input()
petals = petals.split()

petals = [int(x) for x in petals]

nums = 0

for i in range(N):
    sum = 0
    flower_set = set()
    for j in range(i, N):
        # pair(i,j)
        sum += petals[j]
        average = sum/(j-i+1)
        # any flower from [i,j] has average petals
        flower_set.add(petals[j])
        if average in flower_set:
            nums += 1

print(nums)

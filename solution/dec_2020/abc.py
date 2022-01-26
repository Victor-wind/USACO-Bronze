
data = input()
nums_str = data.split()

nums = [ int(x) for x in nums_str]

nums.sort()
#print(num)

if len(nums) != 7:
    print("Wrong input")


# a + b < c ?
if nums[0]+nums[1] == nums[2]:
    print(nums[0], nums[1], nums[3])
else:
    print(nums[0], nums[1], nums[2])



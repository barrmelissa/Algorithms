from operator import methodcaller

#taking i the file input
with open("data.txt") as f:
    nums = f.readlines()
    print nums
nums = [x.strip() for x in nums]
nums = map(methodcaller("split", " "), nums)

nums = [list(map(int, i)) for i in nums] 

print ("New array")
print nums

#insertsort function
def insertsort(nums):

    for cmp_index in range(1, len(nums)):
        cur_index = nums[cmp_index]
        i = cmp_index - 1
        while i >= 0 and cur_index < nums[i - 1]:
            nums[i] = nums[i-1]
            i = i - 1
        nums[i] = cur_index

#printing the results
for index in range(len(nums)):
    insertsort(nums[index])
    print(nums[index])
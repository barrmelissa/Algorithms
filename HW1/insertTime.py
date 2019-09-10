from operator import methodcaller
import time
import random

# with open("data.txt") as f:
#     nums = f.readlines()
#     print nums
# nums = [x.strip() for x in nums]
# nums = map(methodcaller("split", " "), nums)

# nums = [list(map(int, i)) for i in nums] 

# print ("New array")
# print nums

def insertsort(nums):

    for cmp_index in range(1, len(nums)):
        cur_index = nums[cmp_index]
        i = cmp_index - 1
        while i >= 0 and cur_index < nums[i - 1]:
            nums[i] = nums[i-1]
            i = i - 1
        nums[i] = cur_index

        
# # nums = [4, 19, 2, 5, 11]
# # nums = [8, 1, 2, 3, 4, 5, 6, 1, 2]

array1 = []
x = 1000
for l in range(1,11):
    print "#", l, ": Running time for array size:", x
    array1 = random.sample(xrange(10000), x)
    start = time.time()
    array2=insertsort(array1)
    elapsed = (time.time() - start)
    print elapsed, ("seconds\n")
    x = x + 1000




from operator import methodcaller
import time
import random

#taking i the file input
with open("data.txt") as f:
    nums = f.readlines()
    print ("Original Array")
    print nums
nums = [x.strip() for x in nums]
nums = map(methodcaller("split", " "), nums)

nums = [list(map(int, i)) for i in nums] 

print ("\nFormatted array")
print nums

#mergesort function
def mergesort(nums):

    if len(nums) < 2:
        return nums
#from python central************
    if len(nums)>1:
        mid = len(nums)//2
        leftside = nums[:mid]
        rightside = nums[mid:]
#*******************************

        array2 = []


        leftside = mergesort(leftside)
        rightside = mergesort(rightside)
        #while they exist
        while leftside and rightside:
            if leftside[0] < rightside[0]:
                array2.append(leftside[0])
                leftside = leftside[1:]
            else:
                array2.append(rightside[0])
                rightside = rightside[1:]
        #once we go through, one side will be empty, other side needs to be added to total array
        array2 = array2 + leftside + rightside
        return array2


# nums = [4, 19, 2, 5, 11]
# # nums = [8, 1, 2, 3, 4, 5, 6, 1, 2]

array1 = []
x = 1000
for l in range(1,11):
    print "#", l, ": Running time for array size:", x
    array1 = random.sample(xrange(10000), x)
    start = time.time()
    array2=mergesort(array1)
    elapsed = (time.time() - start)
    print elapsed, ("seconds\n")
    x = x + 1000


#!/usr/bin/env python2.7
from operator import methodcaller
import math
import time
import random

#creating an array to hold the sorted array
array2 = []

#mergesort function
def mergesort(nums, a, b):
    #checking if there is just a single number left
    if isinstance(nums, int):
        return nums
    #checking if there is only one element left
    if len(nums) == 1:
        return nums        

    #checking if the array has more than one element in it
    if len(nums)>1:
        #if the array has 4 or more elements, do normally
        if len(nums) >= 4:
            #dividing the list into 4 to set an interval
            interval = len(nums)/4
            #creating 4 sublists each 1/4 of the full list, last one can hold an extra value if the list is odd
            sublists = [nums[0:interval], nums[interval:2*interval], nums[2*interval:3*interval], nums[3*interval:]]

        #if the array has 3 elements, manually assign the sublists
        elif len(nums) == 3:
            interval = len(nums)
            sublists = [[nums[0]], [nums[1]], [nums[2]]]
        #if the array has 2 elements, manually assign the sublists
        elif len(nums) == 2:
            interval = len(nums)
            sublists = [[nums[0]], [nums[1]]]

        #arrays for each 1/4
        a = len(sublists)
        new_array1 = []
        new_array2 = []
        new_array3 = []
        new_array4 = []

        #recursive calls for each 1/4 of the original array
        if len(sublists) >= 1:
            new_array1 = mergesort(sublists[0], a, len(sublists[0]))
        if len(sublists) >= 2:
            new_array2 = mergesort(sublists[1], a, len(sublists[1]))
        if len(sublists) >= 3:
            new_array3 = mergesort(sublists[2], a, len(sublists[2]))
        if len(sublists) >= 4:
            new_array4 = mergesort(sublists[3], a, len(sublists[3]))


        #adding 1/4 of arrays together to sort
        new_array = new_array1 + new_array2 + new_array3 + new_array4

        #if array only has one element, just append it
        if len(new_array) == 1:
            array2.append(new_array)
     
        #setting array2 back to empty
        array2 = []
        #while there are elements in new_array, pick the min
        while len(new_array) > 0:
            #I'm sorry, python 2.7 doesn't have anything for infinity
            min = 10000000000
            #finding the min
            for i in range(len(new_array)):
                if new_array[i] <= min:
                    min = new_array[i]
                    i2 = i
            #appending the found element to the new array
            array2.append(new_array[i2])
            #poping it off since we appended it
            new_array.pop(i2)

        return array2

array1 = []

#records running times with x array size
x = 1000
#prints 10 times with x array size
for l in range(1,11):
    print "#", l, ": Running time for array size:", x
    array1 = random.sample(xrange(10000), x)
    start = time.time()
    array2=mergesort(array1, -1, -1)
    elapsed = (time.time() - start)
    print elapsed, ("seconds\n")
    x = x + 1000





    
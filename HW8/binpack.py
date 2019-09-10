#**************HEADER**************************************************************
#Programmer name: Melissa Barr
#Program name: binpack.py
#Program description: Reads in a text file named bin.txt with multiple test cases and 
# outputs to the terminal the number of bins each algorithm calculated for each test
# case
#Course name: CS372
#Last modified: March 7th, 2019
#**********************************************************************************

import random
import time

#****************firstFit function************
#Description: function that returns the number of bins based on the
# earliest opened bins in which it fits
#Pre-conditions: weight, capacity and lists set
#Post-conditions: filled bins returned
def firstFit(weight, lists, capacity):

    count = 0
    #loops for the amount of weights
    for x in range(0, len(weight)):
        #loops through for the amount of bins
        for i in range(0, len(lists)):
            #if the weight at the current index is less than or equal to the 
            # weight at the current bin, we know it can fit in the bin and we
            # put it in by subtracting that weight from the weight at the current bin
            if weight[x] <= lists[i]:
                lists[i] -= weight[x]
                break
            else:           #if not we continue to loop
                continue
    
    #Note!! Not part of the algorithm
    # loop to return the number of bins we have used
    for x in range(0, len(lists)):
        #if the value is not the capacity value (original value) then we know we have used
        # it and can count it
        if lists[x] != capacity:
            count = count + 1
        else:
            continue
    
    return count

#****************bestFit function************
#Description: function that returns the number of bins by placing
# them in the order in which they arrive and then placing the next
# item into the bin which will leave the least room left over after
# the item is placed in the bin
#Pre-conditions: weight, capacity and lists set
#Post-conditions: filled bins returned
def bestFit(capacity, weight, lists):

    count = 0
    #loop for the amount of weights
    for x in range(0, len(weight)):
        m = 0
        k = 0
        #set the currentWeight
        compareWeight = capacity + 1
        #loop for the amount of bins
        for i in range(0, len(lists)):
            #making sure it will fit
            if lists[i] >= weight[x]:
                
                #if the compareWeight is bigger than the weight at bin[i] - weight[x] and is bigger or equal to 0 then
                # we know that it's better and update compareWeight
                if compareWeight >= lists[i] - weight[x] >= 0:
                    compareWeight = lists[i] - weight[x]
                    m = i
                elif lists[i] == capacity:          #if the bin is equal to the capacity then we know that it is a new bin and can fit
                    m = i                           #our item
                    break
                else:                               #if not, we continue to loop
                    continue
        #assign the item to the best bin
        lists[m] -= weight[x]
    
    #Note!! Not part of the algorithm
    # loop to return the number of bins we have used
    for x in range(0, len(lists)):
        #if the value is not the capacity value (original value) then we know we have used
        # it and can count it
        if lists[x] != capacity:
            count = count + 1
        else:
            continue
    
    return count
           
#****************mergesort function************
#Description: function that returns a sorted list
#Pre-conditions: unsorted list
#Post-conditions: sorted list returned

#CITED: from my previous assignment
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
            if leftside[0] > rightside[0]:
                array2.append(leftside[0])
                leftside = leftside[1:]
            else:
                array2.append(rightside[0])
                rightside = rightside[1:]
        #once we go through, one side will be empty, other side needs to be added to total array
        array2 = array2 + leftside + rightside
        return array2

#******START OF PROGRAM*******
#taking in file and parsing it into array
file = open("bin.txt")
nums = [int(item) for item in file.read().split()]

#setting variables
i = 0
m = 1
count = 1
num_of_test_cases = nums[0]

#run through program for the amount of test cases
for x in range(0, num_of_test_cases):
    #setting variables and arrays
    r = 0
    capacity = nums[i+1]
    numOfItems = nums[i+2]

    index = (i+3)
    weight = []

    #filling weight array
    for x in range(0, int(numOfItems)):
        weight.append(nums[index])
        index = index + 1

    #creating a list of the number of items in the test case
    #initilizing each item in the list to the capacity to start
    lists = [[] for p in xrange(numOfItems)]
    for x in range(0, numOfItems):
        lists[x] = capacity

    #calling first function
    totalBins1 = firstFit(weight, lists, capacity)
    #calling mergesort
    sortedWeight = mergesort(weight)
    #reset bins to 10 each
    for x in range(0, numOfItems):
        lists[x] = capacity
    #caling second function
    totalBins2 = firstFit(sortedWeight, lists, capacity)
    #reset bins to 10 each
    for x in range(0, numOfItems):
        lists[x] = capacity
    #calling third function
    totalBins3 = bestFit(capacity, weight, lists)

    i = index - 1

    #printing results
    print "Test case", m, "First fit:", totalBins1, ", First Fit Decreasing:", totalBins2, ", Best Fit:", totalBins3

    m = m + 1


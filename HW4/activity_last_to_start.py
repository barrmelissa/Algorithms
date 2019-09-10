from operator import methodcaller

#taking in the file input
with open("act.txt") as f:
    nums = f.readlines()
nums = [x.strip() for x in nums]
nums = map(methodcaller("split", " "), nums)

#formatting file input
nums = [list(map(int, i)) for i in nums] 

#algorithm to return the activites
def last_to_start(array2, activites_in_set):
    activities = []
    result = []
    #appending first item since we know it is the last one to start
    activities.append(array2[0][1])
    result.append(array2[0][0])
    n = activites_in_set
    for x in range(1, n):
        k = len(result) - 1
        #checking if there is a conflict
        #start time of the current one we have chosen needs to be greater than the end time of the next one in the array
        if(activities[k] >= array2[x][2]):
            result.append(array2[x][0])
            activities.append(array2[x][1])
        #reverse result back
        reversed_result = []
        for i in reversed(result):
            reversed_result.append(i)
    return reversed_result

#mergesort function, taken from HW1
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
            if leftside[0][1] < rightside[0][1]:
                array2.append(leftside[0])
                leftside = leftside[1:]
            else:
                array2.append(rightside[0])
                rightside = rightside[1:]
        #once we go through, one side will be empty, other side needs to be added to total array
        array2 = array2 + leftside + rightside
        return array2


#rest of the program
num_of_activites = []
#if there are more than 1 item in the array we know it is not the # of activities in the set
for x in range(0, len(nums)):
    if (len(nums[x]) > 1):
        pass
    else:
        #takes all of the #'s of activities in the set and puts them into an array
        num_of_activites.append(nums[x][0])

m = 0
l = 1
#for the total number of sets
for x in range(0, len(num_of_activites)):

    #splitting the original nums array into each set
    index1 = num_of_activites[x] + 1
    set_nums = nums[m:index1 + m]

    #setting the number of actvities and taking it out of the list
    activites_in_set = set_nums[0][0]
    set_nums.pop(0)

    array1 = []
    for x in range(0, activites_in_set):
        array1.append(set_nums[x])
    #sorting the array
    array1 = mergesort(array1)
    #reversing the array
    array2 = []
    for i in reversed(array1):
        array2.append(i)
    #turning the array into a string
    array2Str = " ".join(str(e) for e in array2)

    #calling the function
    result = last_to_start(array2, activites_in_set)
    #printing the results
    print "\nSet", l
    print "Number of activities selected =", len(result)
    final_result = " ".join(str(item) for item in result)
    print "Activites:", final_result

    m = index1 + m
    l += 1



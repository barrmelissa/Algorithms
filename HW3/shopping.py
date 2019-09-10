
#using pseudocode interpreted from knapsack lecture, slide 19
def shoppingSpree(W, i_weight, price, num_items, num_in_family, count, item_number, r):

    #setting max of weight array since we can make our table with the largest weight and then 
    #go back into our table to find the smaller values
    oldW = max(W)
    K = []
    #setting up empty array
    for i in range(num_items + 1):
        K.append([])
    #setting 0's down the first column
    for w in range(oldW + 1):
        K[0].append(0)
    #setting 0's across the first row
    for i in range(1, num_items + 1): 
        K[i].append(0)

        #filling in our table
        for w in range(1, oldW + 1): 
            if i_weight[i-1] <= w:
                #item i can be part of the solution, i_weight is less than the amount we can hold
                #if the price of the one we are looking at plus the last one is greater than the current one
                if price[i-1] + K[i-1][w-i_weight[i-1]] > K[i-1][w]:
                    #use it
                    K[i].append(price[i-1] + K[i-1][w-i_weight[i-1]])
                else:
                    #if not, use the old one
                    K[i].append(K[i-1][w]) 
            else: 
                #i_weight is greater than weight we can hold, so use the old one
                K[i].append(K[i-1][w])
    
    #finding the total price for each family using dynamic programming and finding the total at each weight
    #by indexing through the array and taking the value in the table we have already created, then adding together
    if r == 0:
        totalFam = 0
        p = 0
        #indexing through weight array for the number of members in the family
        for x in range(1, num_in_family+1):
            index = W[p]
            totalFam += K[num_items][index]
            p = p + 1

        #writing output to file
        with open("results.txt", "a") as results:
            results.write("\nTest Case ")
            results.write(str(count))
            results.write("\n")
            results.write("Total Price ")
            results.write(str(totalFam))
            results.write("\n")
            results.write("Member Items:\n")
        results.close()
    else:
        pass

    #setting variables and arrays
    NW = W[r]
    result_array = []
    maxItem = K[num_items][NW]
    c = NW        

    #*****************************************************
    #finding the items taken for each member of the family
    for i in list(reversed(range(1, num_items + 1))):
        #if the max item is equivlent to the item above it, pass we don't need it
        if maxItem == K[i-1][c]:
            pass
        #othewise we take the value at i which is the item number and put it in our result array
        #then we have to de-increment maxItem and c
        else:
            result_array.append(i)
            maxItem -= price[i-1]
            c -= i_weight[i-1]
    #since our array is reversed we reverse it back so it prints correctly
    reversed_array = []
    for i in reversed(result_array):
        reversed_array.append(i)
    #turning the array into a string
    reversed_array = " ".join(str(e) for e in reversed_array)
    #*****************************************************

    #writing our results to file
    with open("results.txt", "a") as results:
        results.write(str(item_number))
        results.write(": ")
        results.write(str(reversed_array))
        results.write("\n")
    results.close()    

    return K[num_items][NW] 

#******START OF PROGRAM*******
#taking in file and parsing it into array
file = open("shopping.txt")
nums = [int(item) for item in file.read().split()]

i = 0
p = 0
l = 2
count = 1
num_of_test_cases = nums[0]

#run through program for the amount of test cases
for x in range(0, num_of_test_cases):
    #setting variables and arrays
    r = 0
    items_in_test_case = nums[i+1]
    price = []
    i_weight = []
    num_in_family = nums[(i+2) + (int(items_in_test_case)*2)]
    W = []
    index = (i+2) + (int(items_in_test_case)*2) + 1
    item_number = 1    
    totalPrice = 0

    #filling price and weight array
    for x in range(0, int(items_in_test_case)):
        price.append(nums[l])
        i_weight.append(nums[l+1])
        l = l + 2

    #filling family members weight array
    for x in range(0, int(num_in_family)):
        W.append(nums[index])
        index = index + 1
 
    i = index - 1
    l = index + 1
 
    #calling shoppingSpree for the number of people in the family
    for x in range(0, num_in_family):
        num_items = len(price) 
        total = shoppingSpree(W, i_weight, price, num_items, num_in_family, count, item_number, r)
        item_number = item_number + 1
        r = r+1
    count = count + 1




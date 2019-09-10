import sys
from operator import methodcaller
import numpy as np

#taking in file as command line argument
with open(sys.argv[1], 'r') as f:
    file_input = f.readlines()

#formating the input
file_input = [x.strip() for x in file_input]
file_input = map(methodcaller("split", " "), file_input)
file_input = [list(map(str, i)) for i in file_input] 

#function to set all 'N' and call DFS_Visit function for each 'N'
#influenced from DFS in lecture
def DFS(Matrix):

    #setting color array to be all 'N' for neutral
    color_array = []
    for x in range(0, len(Matrix)):
        color_array.append('N')
    #if color array at x is 'N' we know we need to determine if they are a babyface or heel
    for x in range(0, len(color_array)):
        if color_array[x] == 'N':
            #call to function
            color_array = DFS_Visit(Matrix, x, x, color_array)

    return color_array

#function to set babyface and heel in color array
#influenced from DFS in lecture
def DFS_Visit(Matrix, x, y, color_array):

    #if color array at x is not 'N' we check if it's the same
    if not color_array[y] == 'N':
        #if the previous determination is the same as the current determination, we know it is not possible
        if color_array[x] == color_array[y]:
            print "No impossible"
            exit()
        else:
            return color_array
    #we set color array at x
    else:
        #if the previous one is 'B' then we set our current one to 'H'
        if color_array[x] == 'B':
            color_array[y] = 'H'
        #if the previous one is 'H' then we set our current one to 'B'
        else:
            color_array[y] = 'B'
        #looping for each remaining item in the matrix, if we find a connection, meaning item == 1
        for i, item in enumerate(Matrix[y]):
            if item == 1:
                #recursively call the function to search the new connection
                color_array = DFS_Visit(Matrix, y, i, color_array)
        return color_array

#setting variables
num_wrestlers = file_input[0][0]
num_rivalries = file_input[int(num_wrestlers)+1][0]

#creating an array for the wrestlers
names_array = file_input[1:int(num_wrestlers)+1]
names_array = np.array(names_array).ravel()

#creating an array for the rivalries
rivalries_array1 = []
rivalries_array1 = file_input[int(num_wrestlers) + 2: int(num_wrestlers)+int(num_rivalries)+2]
rivalries_array1 = np.array(rivalries_array1).ravel()

w = int(num_wrestlers)
h = int(num_wrestlers)
#creating a matrix to hold the rivalries
Matrix = [[0 for x in range(w)] for y in range(w)] 
index1 = 0
index2 = 0
#filling the matrix
for x in range(0, len(rivalries_array1)-1, 2):

    value1 = rivalries_array1[x]
    value2 = rivalries_array1[x+1]
    for y in range(0, len(names_array)):
        #if there is a rivalry
        if names_array[y] == value1:
            index1 = y
    for y in range(0, len(names_array)):
        #if there is a rivalry
        if names_array[y] == value2:
            index2 = y
    #enter 1's where there is a rivalry
    Matrix[index1][index2] = 1
    Matrix[index2][index1] = 1

#calling DFS function
CA = DFS(Matrix)

babyface_results = []
heel_results = []
#indexing through results to determine who is a babyface and who is a heel
for x in range(0, len(CA)):
    if CA[x] == 'B':
        babyface_results.append(names_array[x])
    else:
        heel_results.append(names_array[x])

babyface_results = " ".join(str(item) for item in babyface_results)
heel_results = " ".join(str(item) for item in heel_results)

#printing results
print "Yes Possible"
print "Babyfaces: ", babyface_results
print "Heels: ", heel_results
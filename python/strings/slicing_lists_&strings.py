my_list=[0,1,2,3,4,5,6,7,8,9,10]
        #0,1,2,3,4,5,6,7,8,9,10  positive indexing starting from the left 
      #-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]

print(my_list)
print(my_list[0])
print(my_list[5])
print(my_list[10])
# print(my_list[11])

print(my_list[-1])
print(my_list[-10])


print(my_list[0:6])
print(my_list[3:8])
print(my_list[1:-2]) #last index is not included whether it is posivtive or negative
print(my_list[2:-1]) #last index is not included whether it is posivtive or negative
print(my_list[2:-1:1]) #last index is not included whether it is posivtive or negative
print(my_list[2:-1:2]) #last index is not included whether it is posivtive or negative
print(my_list[2:-1:-1]) #last index is not included whether it is posivtive or negative
print(my_list[-2:1:-1]) #last index is not included whether it is posivtive or negative



print(my_list[-3:1:-1]) #last index is not included whether it is posivtive or negative
print(my_list[-3:1:-2]) #last index is not included whether it is posivtive or negative


print(my_list[::-1]) #printing entire list starting from end to first
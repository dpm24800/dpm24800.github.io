# Though tuple can't be changed directly, there is a workaround. 
# That's convert the tuple into a list, change the list, and convert the list back into a tuple.
tupleX = ('kathmandu', 'surkhet', 'hetauda')
print(f"tupleX=> before change: {tupleX}")

# Convert to list
listX = list(tupleX)

# Modify the list
listX.append('palpa')
listX[1] = 'gaighat'

# Convert back to tuple
tupleX = tuple(listX)
print(f"tupleX=> after change: {tupleX}")
print(f"type(tupleX): {type(tupleX)}")



-------------------------------------------------------------------->

# list to tuple
list = [1, 2, 5]
aa = tuple(list)
print(aa)

# list to tuple
tu = tuple([1, 2, 5])
print(type(tu))


dtX = 1, 2, 3, 4, "dipak"
print(type(dtX))

# A tuple
my_tuple = (1, 2, 3, 4)

# Convert tuple to list
# my_list = list(my_tuple)
# print(my_list)

# though tuple can't be changed directly, there is a workaround.
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tupleX = ('apple', 'banana', 'cherry')
print(f"tupleX=> before change: {tupleX}")

# Convert to list
listX = list(tupleX)

# Modify the list
listX.append('orange')
listX[1] = 'grape'

# Convert back to tuple
tupleX = tuple(listX)
print(f"tupleX=> after change: {tupleX}")
print(f"type(tupleX): {type(tupleX)}")

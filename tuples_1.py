"""
tuple = store multiple items in a single variable
 it is non homogeneous
 ordered
 unchangeable / immutable
 also allows dublication of the values
 we can delete the tuple
"""
myTuple = (1,2,3,4,4, 1, 1.1)
print(myTuple)
print(len(myTuple))

tuple1 = ("apple",4.5) #for single item in tuple program does not consider it a tuple and print it as a string
print(tuple1)

tuple2 = ("car", "bike", "jet", "ship", "boat")
print(tuple2[1])
print(tuple2[1:3])
print(tuple2[:3])

# here we are using typecasting..... = datatype can be changed.

tuple2 = ("car", "bike", "jet", "ship", "boat")
list1 = list(tuple2)   # we changed tuple into list for adding a element in tuple
list1.insert(4,"plane")
tuple3 = tuple(list1)   # we changed list into tuple
print(tuple3)


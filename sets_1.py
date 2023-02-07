""" sets = store multiple values in single variables
            unordered
            unchangable / unmuttable
            can add or clear
            dublicate is not allowed
            hetergenous/non-homogeneous

"""

mySet = {"Car", "Boat", "Train", "Car"}
mySet2={1,2,3,4,5,6}
mySet3={6,7,8,9,10}
print(mySet)

if "Boat" in mySet:
    print(mySet)

mySet.add("bike")
print(mySet)

mySet.update(mySet2)
print(mySet)

mySet.remove("bike")
print(mySet)

print(mySet.pop())  # remove last element
print(mySet)

output = mySet2.union(mySet3)
print(output)

o = mySet2.intersection(mySet3)
print(o)

output1 = mySet2.symmetric_difference(mySet3)
print(output1)

p = mySet2.symmetric_difference_update(mySet3)
print(p)
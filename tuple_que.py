t = (1,2,3,4,5)
list1 = list(t)
list1.reverse()
t2 = tuple(list1)
print(t2) 

t2 = (5,6,7,8,9)
tuple = ("Vaishnavi gupta" ,)
print(tuple)

tuple3 = ("apple", "orange", "pineapple", [1,2,3,4,5])

print(tuple3[3][0],tuple3[2])
tuple3[3][0] = 8
print(tuple3)

tuple7 = tuple+tuple3+t
print(tuple7)

tuple5 = t*t2 #can't multiply
print(tuple5)
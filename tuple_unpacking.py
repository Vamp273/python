# packing and unpacking
tuple = (1,2,3,4,5)
(one, two, three, four, five) = tuple
print(one)
print(two)
print(three)
print(four)
print(five)

tuple1 = ("car", "bike", "boat", "cycle")
(item1, item2, *item3) = tuple1
print(item1)
print(item2)
print(item3)

t = ("car")
(item1, *item2)=t
print(item1)
print(item2)
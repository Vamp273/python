# here we are unpacking the tuple
tuple = (10,20,30,40)
(a,b,c,d) = tuple
print("a =", a)
print(b)
print(c)
print(d)


for i in tuple:
    print(i)

i = 0
while i<len(tuple):
    print(tuple[i])
    i = i+1

tuple1 = (10,20,30,40)
(a,b,c,d)=tuple1
y = (b,c)
print(y)
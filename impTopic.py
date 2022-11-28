# List = can contain different type of a datatype.[heterogeneous data]
l = ["red", "blue", "black", "purple", "pink"]
l[1:5] = ["yellow","orange","violet"]
print(l)


for x in l:
    print(x)

for x in range(len(l)):
    print(l[x])

x=0
while x < len(l):
    print(l[x])
    x+=1
# This is used to compress the list code.

[print(x) for x in l]


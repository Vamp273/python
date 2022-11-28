# collection example is list, tuple, dictionary, set
l = ["red", "blue", "black", "purple", "pink"]
newList = []
for i in l:
    if "a" in i:
        newList.append(i)

print(newList)

newlist=[x.upper() for x in l if x!="pink"]
print(newlist)

l.sort()
print(l)

l.sort(reverse=True)
print(l)
# 1st x in newlist is expression where output came and we can manipuate it
# expression item list condition

number = [1,2,3,4,5]
new = []
for i in number:
    new.append(i**2)
print(new)

number2 = [1,2,3,4,5,2,6]
n = number2.index(2)
number2.pop(n)
number2.insert(n,200)
print(number2)
 
#concatenation can be done only to list not tuple
# concatenation = addition {only with same type of data}

list1 = ["x","y","z"]
list2 = [1,2,3]
"""list3 = list1+list2       # extending the list
print(list3)"""

for i in list1:
    list2.append(i)
print(list2)



#list - it stores multiple items in a single variable
# non homogeneous
#ordered
#Changable / mutable
#allows duplicate values

#append() - add at the end of list
#insert() - insert item at particular index
#extend() - add elements from one list to another
#remove() - remove list element
#pop() - remove with specific index
#del and #clear
#sort() - sort the list in ascending order
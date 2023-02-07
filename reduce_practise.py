# triple all the elements of the list
list1 = [10,20,30,40,50,60]
output = list(map(lambda i : i*i*i, list1))
print(output)

list2 = [34,88,30,22,10,15,18]
output1 = list(lambda i : i%5==0, list2)
print(output1)

output3 = list(filter(lambda i : i%5==0,list2))
print(output3)
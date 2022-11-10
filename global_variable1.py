def count(l):
    even = 0
    odd = 0
    for i in l:
        if i%2==0:
            even +=1
        else:
            odd+=1
    return even, odd

l = [23, 64, 77, 44, 57, 28, 21, 9, 35, 84, 96]

even,odd = count(l)
print(even)
print(odd)
# 0 1 1 2 3 5 8 13[output like this] fibonacci series
# not complete [complete it]
num = int(input())
f = 0
a = 1
if num <= 0:
    print("Series : ", f)
else:
    print(f, a, end=" ")
    for x in range(2,num):
        next = f+a
        print(next,end=" ")
        f = a
        f = next
"""i = int(input("Enter a number = "))
count = 0
while i<=10:
    sum = i+count
    print(sum)"""

count = 0
userInput = int(input())

for i in range(1,userInput+1):
    count = count + i

print("the sum is = ", count)
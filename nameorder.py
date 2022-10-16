x = str(input("Enter your name = "))
length = len(x)
print(length)
if length%2!=0:
    print("middle leter = ", x[int(length//2)])
elif length%2==0:
    print("Middle letter = ", x[(int(length/2)-1)])
    print("Middle letter = ", x[(int(length/2))])

#take string input, print middle index character.
#take string input, if the length of that input > 3 characters then add 'ing' as preffix else print the original input string.
#def add(num1,num2):
    #sum = num1+num2
    #print(sum)
#add(5,6)


#x = lambda num1,num2 : num1+num2
#print(x(3,4))


num = int(input("Enter 1st no. : "))
num1 = int(input("Enter 2nd no. : "))
print("Choose any one arithematic operation = +, -, *, /, **, %")
num2 = str(input("Enter arithematic operation = "))

def opt(num,num1,num2):
    if num2 == "+":
        print(num + num1)
    elif num2 == "-":
        print(num - num1)
    elif num2 == "*":
        print(num * num1)
    elif num2 == "/":
        print(num / num1)
    elif num2 == "**":
        print(num ** num1)
    elif num2 == "%":
        print(num % num1)
    else:
        print("INVALID")

opt(num,num1,num2)
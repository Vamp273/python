num1 = float(input("Enter 1st number = "))
num2 = float(input("Enter 2nd number"))
operator = input("Enter an operator")

if operator == "+":
    print("Sum of the numbers is = ", num1+num2)
elif operator == "-":
    print("Difference of the number is = ", num1-num2)
elif operator == "*":
    print("Multiplication of the number is = ", num1*num2)
elif operator == "/":
    print("Division of the number is = ", num1/num2)
elif operator == "%":
    print("Reminder of the number is = ", num1%num2)
elif operator == "**":
    print("Square of the number is = ", num1**num2)
elif operator == "//":
    print("Quotient of the number is = ", num1//num2)
else:
    print("invalid")
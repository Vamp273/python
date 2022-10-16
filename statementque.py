yearOfService = float(input("Enter your total year of service in this company ="))
currentSalary = float(input("Enter your current salary ="))
bonus = int(1000)
if yearOfService>=5:
    print("Your net bonus is = ", currentSalary+bonus)
else:
    print("OOPS!!! No bonus for you")



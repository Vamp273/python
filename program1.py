salary = float(input("Enter your annual salary ="))
yearOfService = float(input("Enter your total no. of years of service in this company ="))

if yearOfService>10:
    bonus = 0.1*salary
    print("Your encrimented salary is =", bonus+salary)
elif 10>yearOfService>6:
    bonus = 0.8*salary
    print("Your encrimented salary is =", bonus+salary)
elif 0<yearOfService<6:
    bonus = 0.5*salary
    print("Your encrimented salary is =", bonus+salary)
else:
    print("...")
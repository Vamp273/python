#total lecture
#total attendent
#calculate%

numberOfClassesPerMonth = int(input("Enter total no. of working days ="))
numberOfClassesAttendent = int(input("Enter how many classes you have attendent ="))
yourAttendance = (numberOfClassesAttendent/numberOfClassesPerMonth)*100
print("Your attendance is '%' =", yourAttendance)
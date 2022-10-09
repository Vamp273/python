#attendance pecentage.

numberOfClassesPerMonth = int(input("Enter total no. of working days ="))
numberOfClassesAttendent = int(input("Enter how many classes you have attendent ="))
yourAttendance = (numberOfClassesAttendent/numberOfClassesPerMonth)*100
if yourAttendance>75:
    print("Your attendance is =", yourAttendance, "%. You are elligible for exam")
else:
    print("Your attendance is only =", yourAttendance, "%.You are not elligible for exam")


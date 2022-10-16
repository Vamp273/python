# Find AREA OF TRIANGLE by HERON'S formulqa
#Let ABC be a triangle
#PEDMAS = Parentheses, Exponents, division, multipication, addition, subtraction.
a = float(input("Enter length of AB side of a triangle ="))
b = float(input("Enter length of BC side of a triangle ="))
c = float(input("Enter length of CA side of a triangle ="))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(s)
print("the area of triangle ABC is :",area) 
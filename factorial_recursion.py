#doing the same thing on repeat
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
num = fact(25)
print(num)

#square of a number
def sq(x):
    return x**2
x = sq(5)
print(x)

# how to short the length of code... using lambda
y = lambda a : a*a
num = y(5)
print(num)

x = lambda a,b : a*b
num1 = x(5,9)
print(num1)

def name(x):
    return lambda a : a+x
num2 = name(10)
print(num2(5))
def multiply(num1, num2):
    multiply = num1*num2
    return(multiply)

y = multiply(5,9)
print(y)

# no. of. parameters and arguments should be same...

def name(firstName, lastName, age):
    print("My name is ", firstName, lastName, age)
name("Vaishnavi" , "gupta", "19")
name("Jyotsana", "Shyama", "18")

# "*" with parameter is used when we are not sure of no. of arguments...
def name(*args):
    print(args)
name("vaishnavi", "gupta", "yadav")

def name(*args):
    print(args[0])
name("vaishnavi", "gupta", "yadav")

def name(*args):
    print(args[0:2])
name("vaishnavi", "gupta", "yadav")

def name(name, *args):
    print(name)
    print(args)
name("vaishnavi", "gupta", "yadav")
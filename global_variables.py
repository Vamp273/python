a = 5    # global variable
def example():
    a = 10    # local variable
    print(a)
example()
print(a)

# below we are overwriting the value of local a over  global 'a' variable

a = 5
def ex():
    global a
    a = 10
    print(a)
ex()
print(a)

a = 5
def ex():
    global a
    a = 10
    print(a)
print(a)
ex()

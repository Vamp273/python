def name(name1, age):
    print(name1, age)
name("Vaishnavi", "19")

def prac(*value):
    for i in value:
        print(i)
prac("bnhdhd", "hgdfbccj", "bdjnv", "hfjnvk")

def name(firstName="garv", age = 100): # parameters value are default value if argument values are not given
    print("name "+firstName, "age", age)
name("atul")
name("shubam", "101")
# function = using a single same logic again and again...
# print is also a function but it is a builtin function... 
# function require 2 thing 1st definition 2nd naming or calling...
#syntax [defining a function]

def hello():
    print("HELLO WORLD")
    print("HELLO MARS")

hello()  #This is a calling function and hello() is a name of a function


def anime():
    print("romance: your name")
    print("thriller : deathnote")

anime()


# Parameters = jo humne definition me diya hai vo ye hai {num1, num2 is parameter}
# Arguments = jo value hmne calling time diya ho {65, 78 is a argument}


def add(num1, num2):
    sum = num1 + num2
    print(sum)
add(65,78)
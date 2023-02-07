f = open("demo1.txt","r")

a = open("myself.txt", "w")
a.write("HELLO, I am Vaishnavi gupta.\n")
a.write("Currently pursuing CSE from Lovely professional university.\n")
a.write("I am in section KOC28 and my registration no. is 12220425.\n")

for i in f:
    a.write(i)

# This is for closing a file 
f = open("demo.txt")
f.close()

# this is for closing a file if any error occur in the code or writnig a code with error and other code must work.
try:
    f = open("demo.txt")
    # your code goes here and error can occur in her(try) but 
finally:  # file will be closed
    f.close()

# other way to close file properly without calling close() method
with open("demo.txt") as f:
    f.read() # --> example

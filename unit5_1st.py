# this helps us to open any file not just only python file. "r" is for read and "w" is for write and used accordingly whether we
# want to write the file or read the file.

f = open("demo1.txt","r")
print(f.read())

#f1 = open("demo1.txt","a",encoding="utf-8")
#print(f1.read())

#print(f.readline())
#print(f.readline())

# in "w" if file does not exit then it creates the file byitself for us.
a = open("demo2.txt","w")
a.write("This is a new file.")
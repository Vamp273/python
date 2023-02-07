# f = open("demo1.txt","r")
# print(f.read(10))
# print(f.tell())
# print(f.seek())  # Seek for going forward and backward.

f1 = open("LOGO.jpg","rb")  # "rb" = read binary
f2 = open("LOGO_copy.jpg", "wb")   # "wb" = write binary
print(f1.read())

for i in f1:
    f2.write(i)
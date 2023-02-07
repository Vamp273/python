#import os

#if os.path.exists("demo1.txt"):
 #   os.remove("demo1.txt")
#else:
#   print("File does not exit")
#os.remove("demo1.txt")

# try:
    # this block of code will run and throw errors if there are any

# except:
    #this will raise the error

# else:
    # this will execute if there are no errors

#finally:
    #this will execute regardless the result of try and except

try:
    f5=open("example.txt")
    try:
        f5.write("ABC")
    except:
        print("Error in file")

    finally:
        f5.close()
except:
    print("can't open the file")


a = 5
if a<10:
    raise Exception("Value is less than 5")
    
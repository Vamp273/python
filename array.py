# array : it is a type of variable which can store store more than 1 same type data in it.
# array is not available in python,
# but we can use characteristics of array by importing array.

a = "HELLO WORLD"
print(a[6])
print(a[0:9],a[0:5])
print(a [-6:-3])
print(len(a)) # To find length of the string.
b = "a quick brown fox jumps uver the lazy dog"
if "not" in b:  #this is for searing any word or alpahabet from any sentence and its is sensitive so it has to be written in the same way it is written in the sentence.
    print("its there")
else:
    print("No")

if "ox" not in b:   #not in is for the perticular sentence is there it is or not
    print("No")
else:
    print("...")

#[:] it inclue starting but exclude end index value that is written in this[:]
#[:] print start to end of sentence
#[0:] print to the end of sentence
#[:7] print starting to the 6th index
# this is for negative indexing
#a = "HELLO WORLD"
#print(a [-5:-2])
class Laptop:
    def __init__(self):
        self.name = "ASUS"
        self.processor = "i9"

    def printOutput(self):
        print("My Laptop name is :", self.name, "and my proccessor is : ", self.processor)

        #print("ASER","i7","1TB")

laptop1 = Laptop()  # these to are object of Laptop class
laptop2 = Laptop()

print(id(laptop1))
print(id(laptop2))

#laptop1.config()
#laptop2.config()

# instance is where object is created

laptop1.printOutput()
laptop2.printOutput()


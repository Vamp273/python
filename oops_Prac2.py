class Laptop:
    def __init__(self,name,processor):
        self.name = name
        self.processor = processor

    def printOutput(self):
        print("My Laptop name is :", self.name, "and my proccessor is : ", self.processor)

laptop1 = Laptop("DELL","i9")  # these to are object of Laptop class
laptop2 = Laptop("ACER","i7")

laptop1.printOutput()
laptop2.printOutput()
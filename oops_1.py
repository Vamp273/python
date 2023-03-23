x = 5
y = "6"
print(type(y))

class Laptop:
    def config():
        print("i7", "1tb", "16GB")


laptop1 = Laptop
laptop2 = Laptop()
Laptop.config()

laptop1.config()

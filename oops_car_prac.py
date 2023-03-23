class car:

    wheels = 4

    def __init__(self,brand,mil):
        self.brand = brand
        self.mil = mil

car1 = car("BMW", 10)
car2 = car("tesla", 8)

print(car1.brand,car1.mil)
print(car2.brand, car2.mil)

print(car1.brand,car1.mil,car1.wheels)
print(car2.brand, car2.mil,car2.wheels)

car.wheels = 3

print(car1.brand,car1.mil,car1.wheels)
print(car2.brand, car2.mil,car2.wheels)
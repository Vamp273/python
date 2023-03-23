class person:
    def __init__(self):
        self.name = "Shubham"  # name is instance valiable
        self.age = 18
# instance variable = if the variable value varies from object to object then that variable is k/a instance variable 
    def updateName(self,name):
        self.name = name

person1 = person()
person2 = person()

person1.updateName("Vaishnavi")

print(person1.name)
print(person2.name)
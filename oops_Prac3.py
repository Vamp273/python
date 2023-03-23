class person:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def printO(self):
        print("My name is : ",self.name,"and my roll no. is : ",self.rollnumber )

person1 = person("Jyotsana Shyama", "51")
person2 = person("Vaishnavi Gupta", "39")

print(id(person1))
print(id(person2))

person1.printO()
person2.printO()
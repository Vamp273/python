class person:
    def __init__(self):
        self.name = "Vaishnavi"
        self.age = 18

    def compareAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False

person1 = person()
person2 = person()

#person2.name = "Jyotsana" 
person1.age = 18
person2.age = 19

if person1.compareAge(person2):
    print("They are of same age")
else:
    print("They are of different age")

print(person1.name)
print(person2.name)
print(person1.name,person1.age)
print(person2.name,person2.age)
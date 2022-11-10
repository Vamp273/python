l = ["Atul", "shubham", "Anurag", "Rahul", "Dev", "Roy"]

def name(l):
    name1 = 0
    for i in l:
        if len(i)>5:
            name1 += 1
            print(i)
    return name1

name = name(l)
print(name)
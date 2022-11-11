# (**) is for arbitary keyword arguments

def info(name, **data):  #This will form dictionary
    print(name)
    print(data)
info("Vaishnavi", age=26, place="Chandigarh", number=7663933044)

def info(name, **data):
    print(name)
    for i,j in data.items():   #This will form list
        print(i,j)

info("Vaishnavi", age=26, place="Chandigarh", number=7663933044)
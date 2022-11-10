cars = ["Nano", "Ford", "Tata", "BMW", "Thar"]
for i in cars:
    print(i)
    if i == "Tata":
        break  #esme tata esliye print ho rha kyuki 3 baar loop ghum chuka hai aur tata pe jaa chuka hai esliye print ho rha hai

#for i in "HELLO WORLD":
    #print(i)

car = ["Nano", "Ford", "Tata", "BMW", "Thar"]
for i in car:
    if i == "Tata":
        break
    print(i)   #esme tata esliye print nhi hua kyuki 3rd time loop nhi ghumma hai to print nhi hua hai

#once the loop is broken its broken it does not goes to another condition
for i in range(6):
    if i ==3:
        break
    print(i)
else:
    print("Loop is over")
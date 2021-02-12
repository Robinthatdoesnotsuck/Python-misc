curInv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]

newInv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
def func(e):
    return e[1]
def updateInventory(curInv, newInv):
    updateInventory = newInv
    names_new = []
    names_old = []
    for i in curInv:
        for j in newInv:
            if j[1] == i[1]:
                print('vevos')

    for new_item in newInv:
        names_new.append(new_item[1])
    for old_item in curInv:
        names_old.append(old_item[1])
    
    for name in names_old:
        if name in names_new:
            names_old.remove(name)
    print(names_old)
    for name in curInv:
        if name[1] in names_old:
            updateInventory.append(name)
    

    return  updateInventory

print(updateInventory(curInv, newInv))
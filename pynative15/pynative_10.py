list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def createList(list1, list2):
    newList = []
    for i in list1:
        if i % 2 == 1:
            newList.append(i)
    for i in list2:
        if i % 2 == 0:
            newList.append(i)
    return newList

print(createList(list1, list2))
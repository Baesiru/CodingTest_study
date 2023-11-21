myList = []
for i in range(9):
    a = int(input())
    myList.append(a)
print(max(myList))
print(myList.index(max(myList))+1)
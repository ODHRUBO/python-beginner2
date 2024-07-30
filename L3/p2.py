list=[]
list.append(input("a= "))
list.append(input("b= "))
list.append(input("c= "))
list.append(input("d= "))
list.append(input("e= "))
print(list)

list2=list.copy()
print(list2)
list2.reverse()

if list==list2:
    print("palingdrome")
else:
    print("not palingdrome")

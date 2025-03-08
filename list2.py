# menu = ["apple","cherry","banana"]
#append
#pop(1)
#pop()
#remove
#insert
#extend

# x = "Anand"
# menu.insert(1,x)
# print(menu)
# menu.remove("cherry")
# print(menu)
# extra = [1,2,3]
# menu.extend(extra)
# print(menu)

student = []


ch = int(input("press 1 for add item \n press 2 for remove item \n press 3 for display item"))
if ch == 1:
    no = int(input("enter the total item want to add "))
    for i in range(no):
        name = input("enter the name want to add ")
        choice = int(input("press 1 for add item at end \2 press 2 for add item at position "))
        if choice == 1:
            student.append(name)
        elif choice == 2:
            pos = int(input("enter position place "))
            student.insert(pos,name)
        else:
            print("wrong choice")
    print(student)   
elif ch == 2:
    
    ch = int(input("press 1 for remove last \n 2 for remove position \n 3 for remove by name "))
    if ch==1:
        student.pop()
    elif ch==2:
        ind = int(input("enter index no "))
        student.pop(ind-1)
    elif ch==3:
        rem_name = input("enter name want to remove ")
        student.remove(rem_name)
    print(student)
elif ch ==3:
    pass
else:
    print("wrong choice... please try again ")
        

















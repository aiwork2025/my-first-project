#list is mutable, indexed and ordered, allow duplicate value
names = ["Anand",'Amit',"Ankit",'Anand']
print(names)

print(names[0])
print(names[3])
names[1]="talent"
print(names)


names.append("tcit")
print(names)

names.pop()
print(names)

names.pop(2)
print(names)
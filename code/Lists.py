#Lists

l=["Vaibhav","Mojidra","Shreyas","Gurav"]
print(l)
print(type(l))
print(len(l))
print("Mojidra" in l)
print("Shah" in l)
print("mojidra" in l)
print(l[1])
print(l[:2])
print(l[2:])
l2=["Riya","Shah"]
print(l2)
lt=l+l2
print(lt)

#Inserting in list
l.append("Dev")
print(l)
l.insert(1,"Vijesh")
print(l)
l.insert(15,"Vijesh")
print(l)

#Deleting/Removing from list
l.remove('Dev')
print(l)
l.remove('Vijesh')
print(l)
l.pop(3)
print(l)

#Modifying in list
l[3]="Gurav"
print(l)

#Iterting over lists

for i in l:
    print(i)

l3=["SA","SS","SAM"]

#Print along with index:
print(l3)

for i in range(0,len(l3)):
    print(str(i)+" "+l3[i])

print("\n")
#another way of Print along with index

for index,element in enumerate(l3):
    print(str(index)+" "+element)


#List comprehensions
#example we need to have a list with all the numbers between 1-100

#using normal for in range 

s1=[]
for i in range(1,101):
    s1.append(i)
print(s1)

print("\n")

#List comprehensions

s2=[x for x in range(1,101)]
print(s2)

print("\n")

s2=[x for x in range(1,101) if x%2==0]
print(s2)

s2=[x*7 for x in range(1,11)]
print(s2)


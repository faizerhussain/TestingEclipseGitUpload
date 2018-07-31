from array import  *

val1= array('i',[1,2,-4,5,8])
val2= array('u',['a','b','c'])



print(val1)

for i in range(len(val1)):
    print(val1[i])
    
print("***********1")
    
for j in val1:
    print(j)

print("***********2")

val3=array(val1.typecode,(a+a for a in val1))

for j in val3:
    print(j)





    
print("*#######################")    
print(val2)

for i in range(len(val2)):
    print(val2[i])
    
print("***********")
    
for j in val2:
    print(j)
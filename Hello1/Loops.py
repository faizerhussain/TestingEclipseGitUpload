
people = ['john','cena','orton','aj']

for person in people:
    print (person)
    
for i in range(len(people)):
    print('current person is  ',people[i])
    
for i in range(0,10):
    print (i)
    
count =1
while count<10:
    print ('count is  ',count)
    count=count +1
print("********************************************")

    
for i in range(5,16,1):
    print(i)
    
print("********************************************")
    
for i in range(5,16,2):
    print(i)

print("********************************************")
    
for i in range(20,10,-1):
    print(i)
    
print("********************************************")    

for p in range(4):
    for q in range(4):
        print("# ",end="")
    print()
print("********************************************")   

for p in range(4):
    for q in range(p+1):
        print("# ",end="")
    print()

print("********************************************")   

for p in range(4):
    for q in range(4-p):
        print("# ",end="")
    print()
print("********************************************")   

for i in range(4):
    for j in range(4-i):
        print(j + 1, end="")
    print()
print("********************************************") 

t=[1,23,5434,765767,8677567567]    
for p in enumerate(t):
           print(p)

print("********************************************") 

for i,v in enumerate(t):
        print("i={} , value ={}".format(i,v))
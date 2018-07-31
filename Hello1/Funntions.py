
def sayHello(name):
    print('hello', name)
    
sayHello('Faizer')

def sayHello1(name= 'hussain'):
    print('hello', name)
sayHello1()    
sayHello1('Faiz')

def getSum(n1,n2):
    total=n1+n2
    return total

addSum=getSum(2, 3)

print('addition is ',addSum)

print('***************')

def multipleArgumentAddScores(name='tom',*score):
    print(name)
    for s in score:
        print (s)
       

multipleArgumentAddScores('test',1,2)
    

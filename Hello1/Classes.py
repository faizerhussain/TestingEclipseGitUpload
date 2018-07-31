class Person:
    __name =''
    __email=''
    
    def __init__(self,name,email):
        self.__name=name
        self.__email=email 
    
    def setName(self,name):
        self.__name=name
            
    def getName(self):
        return self.__name
    
    def setEmail(self,email):
        self.__email=email
            
    def getEmail(self):
        return self.__email
    
    def toString(self):
        return '{} can be reach at {}'.format(self.__name, self.__email)
        
# faizer=Person()
# faizer.setName('hussain')
# 
# print(faizer.getName())

# faizer=Person('hussain','a@g.com')
# print(faizer.getName())# 
# print(faizer.toString())

class Customer(Person):
    __balance=0
    
    def __init__(self,name, email, balance):
        self.__name=name
        self.__email=email  
        self.__balance=balance
        
        super(Customer,self).__init__(name, email)
        
    def setBalance(self,balance):
        self.__balance=balance
            
    def getBalance(self):
        return self.__balance
    
    def toString(self):
        return '{} has balance of {}  can be reach at {}'.format(self.__name,self.__balance, self.__email)

faiz=Customer('Faiz','a@b.com',100)
faiz.setBalance(200)
print(faiz.toString())
        


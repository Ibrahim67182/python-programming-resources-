class Employee:
    name=""
    age=0
    salary=0.00

    def __init__(self,name):
        self.name=name

    @property
    def getname(self):
        return self.name
    @property    
    def getage(self):
        return self.age
    @property    
    def getsal(self):
        return self.salary
    
    @getage.setter
    def setage(self,a):
     self.age=a    

    @getsal.setter
    def setsal(self,s):
     self.salary=s    



obj= Employee("ibrahim")
obj.setage=21
obj.setsal=77000

print(obj.getname)
print(obj.getage)
print(obj.getsal)





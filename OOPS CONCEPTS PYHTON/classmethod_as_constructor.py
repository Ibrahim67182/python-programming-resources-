
class Person:
    def __init__(self,n,a):
      self.name=n
      self.age=a


    @classmethod 
    def processdata(cls,str):   #this class method works as constructor and resturn the string by breaking it 
       
       name ,age = str.split(" ")

       return cls(name,int(age))
    

p1= Person("ibrahim",21)
print(p1.name)
print(p1.age)

str="Khan 34"
p2=Person.processdata(str)
print(p2.name,p2.age)

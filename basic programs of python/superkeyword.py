
class Parentclass:
    def __init__(self,name):
        
        self.name=name
    
    
    def parent_method(self):
        print("this is parents method")


class Childclass(Parentclass):
    def __init__(self,name):
       
        super().__init__(name)
    
    
    def child_method(self):
        print("this is childs method") 
        super().parent_method()                 #    this keyword is used inside any child function to call the parent method 


par=Parentclass("abbu")
print(par.name)

obj= Childclass("javed")
obj.child_method()               
print(obj.name)
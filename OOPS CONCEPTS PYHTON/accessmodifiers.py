
class Player:
    __name=""     #private var
    __age=""      #private
    _num_goals=0    #protected
    rating=0.0         #public

    def __init__(self):
     self.__name="ibrahim"
     self.__age=20
     self._num_goals=300
     self.rating=5.0

    
    
    
    
obj= Player()

#   it will give error because of private     :   print(obj.__name)
#instead we can write it as


print(obj._Player__name)     #it works fine and this is how you can access private member 
print(obj._Player__age)
print(obj._num_goals)       # no problem with protected member and public directly accessible 
print(obj.rating)      
       


    
    
       

       

def decoration(func):
    def modify_it(*args,**kwargs):
      x=func(*args,**kwargs)
      print(x)
      print("executing decorator func")
      print("i am decorator function to modify your each function!!")
      
    return modify_it


@decoration
def myfunc():
   print("executing my func")
   print("this is example function")


@decoration
def add(n1,n2):  
   print("executing add func") 
   return n1+n2


decoration(myfunc())   # it is equivalent to (decoration(myfunc))()

                    #  if passing args this line will give error        decoration(add)(1,2)


                   #you need to add args and kwargs to handle this  

decoration(add(4,5))                

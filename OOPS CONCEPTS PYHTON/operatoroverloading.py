class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):                                  #to print the object directly
        return f"{self.i} + {self.j} + {self.k}"
    
    def __mul__(self, obj2):                            # this is overloaded defined function for vector multiplication of two objects
        
        return Vector(self.i*obj2.i ,self.j*obj2.j ,self.k*obj2.k)
    






obj1=Vector(3,9,2)
obj2=Vector(5,6,12)

print(obj1)
print(obj2)

print(obj1*obj2)      #this is how operator overloading is performed and you can explore more functions in python official documentation
 
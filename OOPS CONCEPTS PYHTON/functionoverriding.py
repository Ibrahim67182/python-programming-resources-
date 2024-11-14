class Person:
     def info(self,name,age):
          self.name=name
          self.age=age

     def professional(self,sal):
          self.salary=sal
          return self.salary
          

class Pilot(Person):
    def info(self, name, age):
          super().info(name, age)
    

    def professional(self, sal):
         return 30000+ super().professional(sal)   
    
          #we are modifying the function here that pilot has 300k sal 


class Plumber(Person):
     def info(self, name, age):
          super().info(name, age)

     def professional(self, sal):
          return 1200+ super().professional(sal)          
     



pilot_object= Pilot()
pilot_object.info("khan",23)

plumber_object=Plumber()
plumber_object.info("javed",34)

x= plumber_object.professional(300)
y= pilot_object.professional(5000)


print(y, pilot_object.name, pilot_object.age)
print( x,plumber_object.name,plumber_object.age)
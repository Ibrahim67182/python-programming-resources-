class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"the name is {self.name} ")    


class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"the dance is {self.dance}") 

class employeedancer(Employee,Dancer):
    def __init__(self,name,dance):
        Employee.__init__(self,name)
        Dancer.__init__(self,dance)

    def show(self):
        Employee.show(self)
        Dancer.show(self)



em=employeedancer("khan","break")
em.show()
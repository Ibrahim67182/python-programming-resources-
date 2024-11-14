
class Company:
    cname="Microsoft"

    def showname(self):
        print(self.cname)

    @classmethod                        #this is class method and first parameter can be used to access class varibales and change them for every objects
    def changename(self,nname):
        self.cname=nname



e1= Company()   
e2=Company()

e1.showname()
e1.changename("Lenovo")       #this will also change the class name for every object like e2
e2.showname()    
#Function

def functionname():

functionname()

#Class

Class Name:
    def functionnameone():

obj= Name()

#Constructor

class Nameone:
    def __init__(self):
        self.listone=[]
    def functwo(self,one,two):
        self.one=one
        self.two=two
objone=Nameone()
objone.functwo(1,2)

#if
class namet :
    def __init__(self):
        self.listone=[]
    def functhree(self, three,four):
        if three == 3:
            print("it's true")
        else:
            print("it's not true")
objthr=namet()
objthr.functhree(3,4)

#for
class foname:
    def __init__(self):
        self.li=["the","thej", "thejan", "thejanaidu","thejanallani"]
    def funfour(self,name):
        self.name =name
        for i in self.li:
            if i==self.name:
                print("thejanaidunallani")
            else:
                print("just like that thejan")
jlk=foname()
jlk.funfour("thejanaidu")

#1st Principle
class oneprince:
    def __init__(self):
        self.details=[]
    def principleone(self,name,age,city):
    
        if isinstance(name,str) and  isinstance(age,int) and isinstance(city,str):
            self.details.append(name)
            self.details.append(age)
            self.details.append(city)
            
            print("All is well, Theja", self.details)
        else:
            raise TypeError("Datatype error")
        if city == "Bangalore":
            print(city)
        else:
            raise ValueError("Please update location")
    
prince=oneprince( )
prince.principleone("theja",26,"Bangalore")

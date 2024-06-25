class Exponenetial:
    def __init__(self,b=1,e=1) -> None:
        self.base=b
        self.expo=e
    def __mul__(self,obj2):
        if self.base==obj2.base:
            return self.base**(self.expo+obj2.expo)
        else:
            return 'can not multiply'
        
obj1=Exponenetial(2,3)
obj2=Exponenetial(3,5)
print(obj1*obj2)

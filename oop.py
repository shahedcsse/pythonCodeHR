class Product:
    platfrom="Amazon"

    def __init__(self,pid:int,title:str,price:float):
        self.pid=pid
        self.title=title
        self.price=price
        self.secretcode=838293

    @property    #private variable access 
    def secretcode(self)->float:
        return self.__secretcode 

    @secretcode.setter
    def secretcode(self,newcode:int):
        self.__secretcode=newcode

    @secretcode.deleter
    def secretcode(self):
        del self.__secretcode   


    def getPrice(self)-> float:
        return self.price

    def updatePrice(self,newprice:float)->float:
        self.price=newprice 
        return self.price
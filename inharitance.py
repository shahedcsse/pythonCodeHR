#Base class
class produce:
    platfrom = "amazon"


    def __init__(self,pid:str,title:str):
        self.pid=pid
        self.title=title
        self.__code=23323

    def getcode(self ):
        return self.__code

    def __repr__(self):
        return f"product (pid={self.pid},title='{self.title}')"


class cloth(produce):
    def __init__(self,pid:str,title:str,category:str):
        self.category =category
        super().__init__(pid,title)

    def __repr__(self):
        return f"product (pid='{self.pid}',title='{self.title}', category= {self.category})"

class seller:
    def __init__(self, sid:int,s_name:str):
        self.sid=sid
        self.s_name=s_name

    def __repr__(self):
        return f"seller(sid={self.sid},s_name='{self.s_name}')" 


class bottomwere(cloth, seller):
    def __init__(self,pid:str,title:str,category:str,sid:str,s_name:str):
        cloth.__init__(self,pid,title,category)
        seller.__init__(self,sid, s_name)

    def getclothinfo(self):
        return cloth.__repr__(self)

    def getsellerinfo(self):
        return seller.__repr__(self)


b2= bottomwere(233,'Tshirt','dada')  
b2.getclothinfo()                   

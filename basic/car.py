class Car():
    def __init__(self,qash,guyn):
        self.qash=qash
        self.guyn=guyn

class Ccr(Car):
    def __init__ (self,qash,guyn,sharjich):
        super().__init__(qash,guyn)
        self.sharjich=sharjich
    def asa(self):
        print("Im CCR car")
class Evro(Car):
    def __init__(self,qash,guyn,aragutyun):
        super().__init__(qash,guyn)
        self.aragutyun=aragutyun
    def asa(self):
        print("Im Evro car")
class Niva(Ccr):
    def __init__(self,qash,guyn, sharjich,vareliq):
        super().__init__(qash,guyn,sharjich)
        self.vareliq=vareliq
    def asa(self):
        print("Im Niva")
class Mersedes(Evro):
    def __init__(self,qash,guyn,aragutyun,far):
        super().__init__(qash,guyn,aragutyun)
        self.far=far
    def asa(self):
        print("Im Mersedes")
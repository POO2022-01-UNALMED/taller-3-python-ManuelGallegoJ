class Control:

    def __init__(self):
        self.tv = None

    def setTV(self, tv):
	    self.tv = tv	
    def getTv(self):
        return self.tv

    def enlazar(self, tv):
	    self.setTV(tv)
	    tv.setControl(self)

    def turnOn(self):
	    self.tv.turnOn()
    def turnOff(self):
	    self.tv.turnOff()
	
    def setCanal(self, canal):
	    self.tv.setCanal(canal)	
        
    def canalUp(self):
	    self.tv.canalUp(self)
    def canalDown(self):
	    self.tv.canalDown(self)
	
    def volumenUp(self):
	    self.tv.volumenUp(self)
    def volumenDown(self):
	    self.tv.volumenDown(self)

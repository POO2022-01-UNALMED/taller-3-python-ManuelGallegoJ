class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1        
        self.precio = 500
        self.control = None
        self.volumen = 1
        TV.numTV += 1

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    def getControl(self):
	    return self.control
    def setControl(self, control):
	    self.control = control
    def getPrecio(self):
	    return self.precio
    def setPrecio(self, precio):
	    self.precio = precio
    def getVolumen(self):
	    return self.volumen
    def setVolumen(self,  volumen):
        if(self.estado  and volumen <= 7 and volumen >= 0):
            self.volumen = volumen
    def getCanal(self):
	    return self.canal
    def setCanal(self, canal):
	    if(self.estado  and canal <= 120 and canal >= 1):
		    self.canal = canal
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, tv):
        cls.numTV = tv
    def getEstado(self):
	    return self.estado
    def turnOn(self):
	    self.estado = True
    def turnOff(self):
	    self.estado = False
    def canalUp(self):
	    if(self.estado and self.canal < 120):
		    self.canal += 1
    def canalDown(self):
	    if(self.estado and self.canal > 1):
		    self.canal -= 1
    def volumenUp(self):
	    if(self.estado and self.volumen < 7):
		    self.volumen += 1
    def volumenDown(self):
	    if(self.estado and self.volumen > 0):
		    self.volumen -= 1
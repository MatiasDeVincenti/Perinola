class Apuesta:
    ##constructor 
    def __init__(self):
        self.fichas = 0
    ##funcion para mostrar el print
    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas" 
    
    def ponerFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas
    
    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f"No alcanza para sacar {cuantas} fichas.  Hay solo {self.fichas}")
        self.fichas = self.fichas - cuantas

    def tomarTodas(self):
        if self.fichas == 0:
            raise ValueError(f"No alcanza para sacar fichas.  Hay solo {self.fichas}")
        self.fichas = 0
        return self.fichas 